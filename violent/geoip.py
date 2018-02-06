import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def print_record(tgt):
    rec = gi.record_by_name(tgt)
    print(rec)


print_record('173.255.226.98')
