__author__ = 'lrowell'
import requests
import xml.etree.ElementTree as ET

missingData = open('missingData', 'w')
missingImage = open('missingImage', 'w')

#CarCategories are 1-18
#CarTypes 1-22

#carPickupCountries = ['','ARM','MAC','DOM','TCA','MYS','VEN','LTU','URY','GTM','TZA','SWZ','CHF','DZA','MWI','ARE','NCL','SGP','BRB','PRT','BOL','BWA','QAT','VUT','GAB','SLB','PRY','MNG','ANT','LSO','ISL','FRO','LVA','MCO','BLZ','GBR','KEN','HUN','TUN','PER','SVK','CYM','TWN','CAN','GUM','SLV','SYR','UKR','ASM','SXM','MUS','POL','GLP','AIA','COL','CYP','GIN','AUT','RUS','JAM','ZMB','IRL','ESP','BLR','CUB','ALB','SVN','GUF','MOZ','AGO','GNQ','ECU','BHS','ROU','GMB','SAU','GRL','NZL','GHA','ISR','GIB','ZWE','LUX','MTQ','KNA','NAM','JPN','MRT','HND','SRB','YEM','BGD','BRA','ZAF','MDA','MLI','LAO','MDG','BEN','BHR','MEX','NLD','SCG','ETH','MAF','CAF','NOR','MLA','NGA','HKG','PRI','PAN','IRQ','AZE','   ','GEO','KHM','CPV','IRN','BES','JOR','SUR','PLW','HTI','COD','BRN','MLT','BDI','CHN','TGO','LBN','DNK','MNE','IND','GRD','MYT','VNM','OMN','TUR','PYF','HRV','MNP','LCA','TTO','THA','GRC','SWE','COG','EGY','CMR','ATG','CIV','BGR','CRI','SYC','UGA','ARG','IDN','BFA','BEL','KWT','CZE','NIU','DJI','DEU','EST','AUS','VGB','REU','PHL','FRA','NIC','SEN','CHL','KOR','USA','NER','ITA','DMA','LKA','COK','KAZ','BIH','SDN','BLM','FJI','PAK','VIR','CHE','MKD','CUW','FIN','PNG','WSM','TCD','AND','LBY','MAR','ABW','RWA']
carPickupCountries = ['']
carCategoryTypes = [(0,1), (1,1), (1,2), (1,3), (1,4), (1,5), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12), (1,13), (1,14), (1,16), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10), (2,11), (2,12), (2,13), (2,14), (2,16), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9), (3,10), (3,11), (3,12), (3,13), (3,14), (3,16), (3,17), (3,18), (3,22), (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (4,10), (4,11), (4,12), (4,13), (4,14), (4,15), (4,16), (4,18), (4,22), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10), (5,11), (5,12), (5,13), (5,14), (5,15), (5,17), (5,19), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9), (6,10), (6,11), (6,12), (6,13), (6,14), (6,15), (6,16), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9), (7,10), (7,11), (7,12), (7,13), (7,14), (7,17), (7,21), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,11), (8,12), (8,13), (8,14), (8,17), (8,21), (8,22), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9), (9,10), (9,11), (9,12), (9,13), (9,14), (9,16), (9,17), (9,20), (9,21), (10,2), (10,8), (10,13), (10,14), (11,1), (11,2), (11,10), (11,13), (11,14), (12,1), (12,3), (12,5), (12,8), (12,10), (12,13), (12,14), (13,3), (13,4), (13,5), (13,8), (13,9), (13,14), (14,3), (14,8), (14,10), (14,14), (14,19), (15,3), (15,4), (15,10), (15,14), (15,15), (16,3), (16,4), (16,5), (16,7), (16,8), (16,9), (16,10), (16,13), (16,14), (16,17), (17,1), (17,2), (17,3), (17,4), (17,7), (17,8), (17,9), (17,10), (17,11), (17,13), (17,17), (17,21), (18,4), (18,10), (18,13)]
#langIDs = ['','1028','1030','1031','1033','1035','1036','1040','1043','1044','1046','1053','1057','1086','1124','2057','2058','2060','2067','3081','3082','3084','4105','5129','11274']

smallImages = dict()
largeImages = dict()

#Create loop and Maserati get requests
for carCategoryType in carCategoryTypes:
    carCategory = carCategoryType[0]
    carType = carCategoryType[1]
    for carPickupCountry in carPickupCountries:
            #for langID in langIDs:
                #print (r'http://carbsint:52008/media/search?clientcode=1FX936&cartypecode=' + str(carType) + r'&carcategorycode=' + str(carCategory) + r'&languageid=' + langID + r'&carpickupcountry=' + carPickupCountry )
            url = r'http://carbsint:52008/media/search?clientcode=1FX936&cartypecode=' + str(carType) + r'&carcategorycode=' + str(carCategory) + r'&carpickupcountry=' + carPickupCountry
            r = requests.get(url)
            root = ET.fromstring(r.text)
            mediaInfo = root.find('{urn:com:expedia:s3:cars:messages:media:search:defn:v1}CarMediaInformationList/{urn:com:expedia:s3:cars:messages:media:search:defn:v1}CarMediaInformation')
            if mediaInfo:
                #missingData.write(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry + '\n')
            #else:
                smallImage = mediaInfo.find('{urn:expedia:e3:data:cartypes:defn:v5}CarCatalogMakeModel/{urn:expedia:e3:data:cartypes:defn:v5}ImageThumbnailFilenameString')
                largeImage = mediaInfo.find('{urn:expedia:e3:data:cartypes:defn:v5}CarCatalogMakeModel/{urn:expedia:e3:data:cartypes:defn:v5}ImageFilenameString')
                smallImagePath = r'http://images.trvl-media.com/cars'+smallImage.text
                largeImagePath = r'http://images.trvl-media.com/cars'+largeImage.text
                print(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry)
                print(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry)

                if not smallImages.get(smallImagePath):
                    smallImages[smallImagePath] = [str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry]
                else:
                    smallImages[smallImagePath].append(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry)

                if not largeImages.get(largeImagePath):
                    largeImages[largeImagePath] = [str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry]
                else:
                    largeImages[largeImagePath].append(str(carCategory)+', ' + str(carType) + ', ' + carPickupCountry)

for imagePath in smallImages.keys():
    status = requests.get(imagePath).status_code
    if status == 404:
        missingImage.write(imagePath + '\n')

missingData.close()
missingImage.close()