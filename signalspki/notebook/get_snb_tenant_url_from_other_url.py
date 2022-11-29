## Retrieve the basic tenant URL from the URL of one of its elements
def get_snb_tenant_url_from_other_url(url: str, snb_domain='signalsnotebook.perkinelmercloud') -> str:
    # initialise output variable
    snb_url = ''
    # split the URL ath the (signalsnotebook) and build the pieces
    url_split = url.split(snb_domain)
    # take the first part of the domain
    snb_url = snb_url + url_split[0]
    # attach the fixed domain part
    snb_url = snb_url + snb_domain
    # retrieve the "country" id
    url_split2 = url_split[1].split('.')
    url_split3 = url_split2[1].split('/')
    snb_url = snb_url + '.' + url_split3[0]
    return(snb_url)