# vendor_preview.py

from firm_clio.clio_client import get_clio_client
from clio_sdk.api.contacts_api import ContactsApi
from utils.paginator import ClioPaginator


def preview_vendor_sync(limit=None):
    print("\n🔍 Previewing Clio contacts for vendor sync...\n")

    client = get_clio_client()
    api = ContactsApi(client)

    paginator = ClioPaginator(api.contact_index_with_http_info, page_size=200)

    total_candidates = 0
    total_previewed = 0
    page_num = 0

    for page in paginator.pages():
        page_num += 1
        page_candidates = 0

        for contact in page:
            total_previewed += 1

            if getattr(contact, "matters_count", 0) > 0:
                continue

            contact_id = contact.id
            name = contact.name or "—"

            print(f" • {name:<30} (ID: {contact_id})")
            page_candidates += 1
            total_candidates += 1

            if limit and total_candidates >= limit:
                break

        print(f"\n🔚 Page {page_num} complete. Displayed {page_candidates} vendor candidates.\n")

        if limit and total_candidates >= limit:
            break

    print(f"✅ Done. Previewed {total_previewed} contacts across {page_num} page(s).")
    print(f"✅ Total vendor candidates: {total_candidates}")
