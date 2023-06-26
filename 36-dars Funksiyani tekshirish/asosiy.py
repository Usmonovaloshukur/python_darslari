
def get_fullname(ism,familya,otasi=''):
    if otasi:
        return f"{ism} {familya} {otasi}".title()
    else:
        return f"{ism} {familya}".title()



