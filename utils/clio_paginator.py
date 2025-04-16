class ClioPaginator:
    def __init__(self, api_func, pagination_mode='cursor', per_page=200, **kwargs):
        """
        pagination_mode: 'cursor' or 'offset'
        """
        self.api_func = api_func
        self.mode = pagination_mode
        self.limit = per_page
        self.params = kwargs
        self.params["limit"] = per_page
        self.params["order"] = "id(asc)" if self.mode == "cursor" else kwargs.get("order", None)

        self.page = 0
        self.offset = 0
        self.next_url = None
        self.done = False

    def _parse_next_url(self, response):
        if hasattr(response, "raw_data"):
            return response.raw_data.get("meta", {}).get("paging", {}).get("next")
        return None

    def _extract_query_params(self, url):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(url)
        return {k: v[0] for k, v in parse_qs(parsed.query).items()}

    def next_page(self):
        if self.done:
            return None

        if self.mode == "offset":
            self.params["offset"] = self.offset

        response = self.api_func(**self.params)
        data = response.data

        if not data or len(data) == 0:
            self.done = True
            return []

        self.page += 1
        self.offset += self.limit

        if self.mode == "cursor":
            self.next_url = self._parse_next_url(response)
            if self.next_url:
                self.params.update(self._extract_query_params(self.next_url))
            else:
                self.done = True
        elif self.mode == "offset" and self.offset >= 10000:
            self.done = True

        return data

    def has_next(self):
        return not self.done

    def reset(self):
        self.page = 0
        self.offset = 0
        self.next_url = None
        self.done = False
