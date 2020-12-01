# External Libraries
import vobject

def createVCard(first_name: str = None, last_name : str = None,
  email = None, email_type = None, tel = None, tel_type = None,
  address = None, address_type = None,url: str = None, title: str = None,
  company: str = None, company_group: str = "") -> vobject.vCard:
    
    vc = vobject.vCard()
    
    if first_name or last_name:
        vc.add("n")
        vc.n.value = vobject.vcard.Name( family=last_name, given=first_name )
        vc.add('fn')
        vc.fn.value =f"{first_name} {last_name}"


    if email and email_type:
        if isinstance(email, (list,tuple)) and isinstance(email_type, (list,tuple)):
            for i, (e, etype) in enumerate(zip(email, email_type)):
                vc.add('email')
                vc.email_list[i].value = e
                vc.email_list[i].type_param = etype
        elif isinstance(email, str) and isinstance(email_type, str):
                vc.add("email").value = email
                vc.email.type_param = email_type
    
    if tel and tel_type:
        if isinstance(tel, (list,tuple)) and isinstance(tel_type, (list,tuple)):
            for i, (t, ttype) in enumerate(zip(tel, tel_type)):
                vc.add('tel')
                vc.tel_list[i].value = t
                vc.tel_list[i].type_param = ttype
        elif isinstance(tel, str) and isinstance(tel_type, str):
                vc.add("tel").value = tel
                vc.tel.type_param = tel_type

    if address and address_type:
        if isinstance(address, (list,tuple)) and isinstance(address_type, (list,tuple)):
            for i, (add, addtype) in enumerate(zip(address, address_type)):
                vc.add('adr')
                vc.adr_list[i].value = add
                vc.adr_list[i].type_param = addtype
        elif isinstance(address, vobject.vcard.Address) and isinstance(address_type, str):
                vc.add("adr").value = address
                vc.tel.type_param = address_type   

    if url:
        vc.add("url").value = url

    if title:
        vc.add("title").value = title

    if company:
        vc.add("org").value = [company,company_group]

    print(vc.prettyPrint())

    return vc
