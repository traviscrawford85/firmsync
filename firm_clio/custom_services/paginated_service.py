from firm_clio.utils.pagination import ClioPaginator
from typing import Callable, Generator, Any

class PaginatedService:
    """
    Base class to add reusable pagination logic to any Clio service class.
    """

    def paginate(self, api_func: Callable, page_size: int = 100, **params) -> Generator[Any, None, None]:
        """
        Yields individual records from a paginated Clio API call.

        :param api_func: A callable like ContactsApi.contact_index
        :param page_size: Number of items per page
        :param params: Query parameters (e.g., filters)
        """
        paginator = ClioPaginator(api_func, page_size=page_size, **params)
        for item in paginator:
            yield item

    def paginate_pages(self, api_func: Callable, page_size: int = 100, **params) -> Generator[list[Any], None, None]:
        """
        Yields full pages from a paginated Clio API call.
        """
        paginator = ClioPaginator(api_func, page_size=page_size, **params)
        for page in paginator.pages():
            yield page
