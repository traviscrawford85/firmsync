from typing import List, Generator
from clio_sdk.api.contacts_api import ContactsApi
from firm_clio.custom_models.contact import ContactModel
from firm_clio.clio_client import get_clio_client
from firm_clio.custom_services.paginated_service import PaginatedService


class ContactService(PaginatedService):
    """
    Service for handling Clio contact operations using PaginatedService.
    """

    def __init__(self):
        self.client = get_clio_client()
        self.api = ContactsApi(self.client)

    def get_all_contacts(self) -> List[ContactModel]:
        """
        Returns all contacts using pagination.
        """
        return [self._parse_contact(contact) for contact in self.paginate(self.api.contact_index)]

    def yield_contacts(self) -> Generator[ContactModel, None, None]:
        """
        Yields one contact at a time using the paginator.
        """
        for contact in self.paginate(self.api.contact_index):
            yield self._parse_contact(contact)

    def get_contact_by_id(self, contact_id: int) -> ContactModel:
        item = self.api.contact_show(contact_id).data
        return self._parse_contact(item)

    def _parse_contact(self, item) -> ContactModel:
        return ContactModel(
            id=item.id,
            etag=item.etag,
            name=item.name,
            first_name=item.first_name,
            middle_name=item.middle_name,
            last_name=item.last_name,
            date_of_birth=item.date_of_birth,
            type=item.type,
            created_at=item.created_at,
            updated_at=item.updated_at,
            prefix=item.prefix,
            title=item.title,
            initials=item.initials,
            clio_connect_email=item.clio_connect_email,
            locked_clio_connect_email=item.locked_clio_connect_email,
            client_connect_user_id=item.client_connect_user_id,
            primary_email_address=item.primary_email_address,
            secondary_email_address=item.secondary_email_address,
            primary_phone_number=item.primary_phone_number,
            secondary_phone_number=item.secondary_phone_number,
            ledes_client_id=item.ledes_client_id,
            has_clio_for_clients_permission=item.has_clio_for_clients_permission,
            is_client=item.is_client,
            is_clio_for_client_user=item.is_clio_for_client_user,
            is_co_counsel=item.is_co_counsel,
            is_bill_recipient=item.is_bill_recipient,
            sales_tax_number=item.sales_tax_number,
            currency=item.currency,
        )
