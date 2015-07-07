__author__ = 'lrowell'
import requests
import xml.etree.ElementTree as ET

missingData = open('missingData', 'w')
missingImage = open('missingImage', 'w')

#CarCategories are 1-18
#CarTypes 1-22

carPickupCountries = ['','ARM','MAC','DOM','TCA','MYS','VEN','LTU','URY','GTM','TZA','SWZ','CHF','DZA','MWI','ARE','NCL','SGP','BRB','PRT','BOL','BWA','QAT','VUT','GAB','SLB','PRY','MNG','ANT','LSO','ISL','FRO','LVA','MCO','BLZ','GBR','KEN','HUN','TUN','PER','SVK','CYM','TWN','CAN','GUM','SLV','SYR','UKR','ASM','SXM','MUS','POL','GLP','AIA','COL','CYP','GIN','AUT','RUS','JAM','ZMB','IRL','ESP','BLR','CUB','ALB','SVN','GUF','MOZ','AGO','GNQ','ECU','BHS','ROU','GMB','SAU','GRL','NZL','GHA','ISR','GIB','ZWE','LUX','MTQ','KNA','NAM','JPN','MRT','HND','SRB','YEM','BGD','BRA','ZAF','MDA','MLI','LAO','MDG','BEN','BHR','MEX','NLD','SCG','ETH','MAF','CAF','NOR','MLA','NGA','HKG','PRI','PAN','IRQ','AZE','   ','GEO','KHM','CPV','IRN','BES','JOR','SUR','PLW','HTI','COD','BRN','MLT','BDI','CHN','TGO','LBN','DNK','MNE','IND','GRD','MYT','VNM','OMN','TUR','PYF','HRV','MNP','LCA','TTO','THA','GRC','SWE','COG','EGY','CMR','ATG','CIV','BGR','CRI','SYC','UGA','ARG','IDN','BFA','BEL','KWT','CZE','NIU','DJI','DEU','EST','AUS','VGB','REU','PHL','FRA','NIC','SEN','CHL','KOR','USA','NER','ITA','DMA','LKA','COK','KAZ','BIH','SDN','BLM','FJI','PAK','VIR','CHE','MKD','CUW','FIN','PNG','WSM','TCD','AND','LBY','MAR','ABW','RWA']

#langIDs = ['','1028','1030','1031','1033','1035','1036','1040','1043','1044','1046','1053','1057','1086','1124','2057','2058','2060','2067','3081','3082','3084','4105','5129','11274']

#Create loop and Maserati get requests
for carCategory in range(1, 18):
    for carType in range(1, 22):
        for carPickupCountry in carPickupCountries:
            #for langID in langIDs:
                #print (r'http://carbsint:52008/media/search?clientcode=1FX936&cartypecode=' + str(carType) + r'&carcategorycode=' + str(carCategory) + r'&languageid=' + langID + r'&carpickupcountry=' + carPickupCountry )
            url = r'http://carbsint:52008/media/search?clientcode=1FX936&cartypecode=' + str(carType) + r'&carcategorycode=' + str(carCategory) + r'&carpickupcountry=' + carPickupCountry
            r = requests.get(url)
            root = ET.fromstring(r.text)
            mediaInfo = root.find('{urn:com:expedia:s3:cars:messages:media:search:defn:v1}CarMediaInformationList/{urn:com:expedia:s3:cars:messages:media:search:defn:v1}CarMediaInformation')
            if not mediaInfo:
                missingData.write(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry + '\n')
            else:
                smallImage = mediaInfo.find('{urn:expedia:e3:data:cartypes:defn:v5}CarCatalogMakeModel/{urn:expedia:e3:data:cartypes:defn:v5}ImageThumbnailFilenameString')
                largeImage = mediaInfo.find('{urn:expedia:e3:data:cartypes:defn:v5}CarCatalogMakeModel/{urn:expedia:e3:data:cartypes:defn:v5}ImageFilenameString')
                smallImagePath = r'http://images.trvl-media.com/cars'+smallImage.text
                largeImagePath = r'http://images.trvl-media.com/cars'+largeImage.text
                st1 = requests.get(smallImagePath).status_code
                st2 = requests.get(largeImagePath).status_code
                if not st1 == requests.codes.ok:
                    missingImage.write(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry + ' thumbnail ' + smallImagePath + ', ' + str(st1) + '\n')
                if not st1 == requests.codes.ok:
                    missingImage.write(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry + ' image ' + largeImagePath + ', ' + str(st2) + '\n')

missingData.close()
missingImage.close()