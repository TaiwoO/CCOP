# This script loads some hard coded values into the database

import sys
sys.path.insert(0, '../')

from app import app, db, Crime, Arrest

fake_crimes = []

fake_crimes.append(
    Crime(
        address_number="8100",
        agency="MCPD",
        beat="3G1",
        case_number="14041165",
        city="SILVER SPRING",
        date="2014-08-25T20:04:00.000",
        district="SILVER SPRING",
        longitude=-77.026729,
        latitude=38.990268,
        geolocation_address="8100 GEORGIA AVE",
        geolocation_city="SILVER SPRING",
        geolocation_state="MD",
        geolocation_zip="20910",
        incident_id="200986023",
        incident_type="2791",
        location="8100 GEORGIA AVE",
        narrative="ALL OTHER NON-TRAFFIC CRIM OFFENSES",
        place="Street - Commercial",
        police_district_number="3D",
        pra="94",
        sector="G",
        start_date="2014-08-25T20:04:00.000",
        state="MD",
        zip_code="20910"
    )
)

fake_crimes.append(
    Crime(
        address_number="10100",
        agency="MCPD",
        beat="2D3",
        case_number="14042282",
        city="KENSINGTON",
        date="2014-09-01T13:09:00.000",
        district="BETHESDA",
        # end_date="2014-08-31T06:30:00.000",
        longitude=-77.085521,
        latitude=39.020808,
        geolocation_address="10100 CEDAR LN",
        geolocation_city="KENSINGTON",
        geolocation_state="MD",
        geolocation_zip="20895",
        incident_id="200986810",
        incident_type="617",
        location="10100 CEDAR LN",
        narrative="LARCENY FROM BUILDING OVER $200",
        place="Residence - Shed",
        police_district_number="2D",
        pra="180",
        sector="D",
        start_date="2014-08-31T00:00:00.000",
        state="MD",
        zip_code="20895"
    )
)


fake_crimes.append(
    Crime(
        address_number="12500",
        agency="MCPD",
        beat="4K2",
        case_number="14041909",
        city="SILVER SPRING",
        date="2014-08-29T22:29:00.000",
        district="WHEATON",
        longitude=-77.071767,
        latitude=39.06115,
        geolocation_address="12500 GOODHILL RD",
        geolocation_city="SILVER SPRING",
        geolocation_state="MD",
        geolocation_zip="20906",
        incident_id="200986526",
        incident_type="433",
        location="12500 GOODHILL RD",
        narrative="AGG ASSLT OTHER WPN SPOUSE/PARTNER",
        place="Street - Residential",
        police_district_number="4D",
        pra="334",
        sector="K",
        start_date="2014-08-29T22:29:00.000",
        state="MD",
        zip_code="20906"
    )
)

fake_crimes.append(
    Crime(
        address_number="20400",
        agency="MCPD",
        beat="5N1",
        case_number="14041720",
        city="GERMANTOWN",
        date="2014-08-28T20:19:00.000",
        district="GERMANTOWN",
        # end_date="2014-08-28T08:45:00.000",
        longitude=-77.281214,
        latitude=39.189236,
        geolocation_address="20400 WATERS POINT LN",
        geolocation_city="GERMANTOWN",
        geolocation_state="MD",
        geolocation_zip="20874",
        incident_id="200986382",
        incident_type="634",
        location="20400 WATERS POINT LN",
        narrative="LARCENY FROM AUTO UNDER $50",
        place="Parking Lot - Residential",
        police_district_number="5D",
        pra="465",
        sector="N",
        start_date="2014-08-27T14:00:00.000",
        state="MD",
        zip_code="20874"
    )
)

with app.app_context():
    for crime in fake_crimes:
        db.session.add(crime)
    db.session.commit()
