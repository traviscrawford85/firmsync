from urllib.parse import urlparse, parse_qs


class ClioPaginator:
    def __init__(self, api_func, page_size=200, mode="cursor", **initial_params):
        """
        Generic paginator for Clio API.

        Args:
            api_func: The Clio SDK function to call (e.g., ContactsApi.contact_index_with_http_info)
            page_size: Number of items per page (default 200)
            mode: 'cursor' (recommended) or 'offset'
            **initial_params: Any additional params for the API (filters, fields, etc.)
        """
        self.api_func = api_func
        self.mode = mode
        self.page_size = page_size
        self.params = initial_params or {}
        self.params["limit"] = self.page_size

        if self.mode == "cursor":
            self.params["order"] = "id(asc)"  # Required for cursor-based pagination
            self._offset = None
        elif self.mode == "offset":
            self._offset = 0
            self.params["offset"] = self._offset

        self._done = False
        self._page_count = 0
        self._buffer = []
        self._next_url = None

    def _extract_next_page_params(self, next_url: str):
        """
        Parses the next page URL and updates the internal parameters for the next request.
        """
        parsed_url = urlparse(next_url)
        query_params = parse_qs(parsed_url.query)
        for key, value in query_params.items():
            self.params[key] = value[0]

    def _fetch_next_page(self):
        if self._done:
            return

        response = self.api_func(**self.params)

        # Handle ApiResponse wrapping
        result_data = getattr(response, "data", response)

        # Handle pagination
        next_page = None
        if hasattr(result_data, "meta") and hasattr(result_data.meta, "paging"):
            next_page = getattr(result_data.meta.paging, "next", None)

        # Normalize result to a list of items
        if hasattr(result_data, "data") and isinstance(result_data.data, list):
            self._buffer = result_data.data
        elif isinstance(result_data, list):
            self._buffer = result_data
        else:
            self._buffer = []

        self._page_count += 1

        # Update pagination state
        if self.mode == "cursor":
            if next_page:
                self._extract_next_page_params(next_page)
            else:
                self._done = True
        elif self.mode == "offset":
            self._offset += self.page_size
            self.params["offset"] = self._offset
            if not self._buffer:
                self._done = True

    def __iter__(self):
        return self

    def __next__(self):
        while not self._buffer and not self._done:
            self._fetch_next_page()

        if not self._buffer:
            raise StopIteration

        return self._buffer.pop(0)

    def pages(self):
        """
        Generator for fetching one page at a time.
        """
        while not self._done:
            self._fetch_next_page()
            if not self._buffer:
                break
            yield self._buffer
            self._buffer = []

    def reset(self):
        """
        Reset the paginator (useful if you want to iterate again)
        """
        self._offset = 0 if self.mode == "offset" else None
        self._done = False
        self._page_count = 0
        self._buffer = []
        self._next_url = None

# Enable paginator to write to sqlite db
def cache_matters(conn, matter):
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO matters (id, display_number, description)
        VALUES (?, ?, ?)
    """, (matter.id, matter.display_number, matter.description))
    conn.commit()
