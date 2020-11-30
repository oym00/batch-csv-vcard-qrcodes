import qrcode, vobject


# Making the vCard
vc = vobject.vCard()

vc.add("n")
vc.n.value = vobject.vcard.Name( family='Harris', given='Jeffrey' )
vc.add('fn')
vc.fn.value ='Jeffrey Harris'

vc.add('email')
vc.email.value = 'jeffrey@osafoundation.org'
vc.email.type_param = 'WORK'

vc.add('tel').value = '+1 (604)777-1234'
vc.tel_list[0].type_param = "WORK"
vc.add('tel').value = '229'
vc.tel_list[1].type_param = "EXT"

vc.add("adr").value = vobject.vcard.Address(street='101A - 1337 Street Ave', city='Coquitlam', region='British Columbia', code='V3L 1L1', country='Canada')
vc.adr.type_param = "WORK"

vc.add("url").value = "https://www.ewbsite.org"

vc.add("title")
vc.title.value = "Lead Project Manager"

vc.add("org")
vc.org.value = ["Creative Transportation Solutions Ltd","Engineering Group"]

vc.prettyPrint()

print(vc.serialize())


# Making the QR Code
qr = qrcode.QRCode(border=1)

qr.add_data(vc.serialize())

qr.make()

img = qr.make_image()

img.save("output/name.png")