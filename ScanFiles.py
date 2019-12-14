import json
import os

def read_file(path):
    with open(path, 'r') as json_file:
        data = json.load(json_file)

    study = data['FullStudy']['Study']
    protocol_selection = study['ProtocolSection']
    identification_module = protocol_selection['IdentificationModule']

    if 'OversightModule' not in study:
        return

    oversight =  study['OversightModule']
    
    # data
    nctId = identification_module['NCTId']
    orgStudyId = identification_module['OrgStudyIdInfo']['OrgStudyId']
    orgFullName = protocol_selection['Organization']['OrgFullName']
    overallStatus = study['StatusModule']['OverallStatus']
    startDate = study['StartDateStruct']['StartDate']
    primaryCompletionDate = study['PrimaryCompletionDateStruct']['PrimaryCompletionDate']
    completionDate = study['CompletionDateStruct']['CompletionDate']
    isFDARegulatedDrug = oversight['IsFDARegulatedDrug']
    isFDARegulatedDevice = oversight['IsFDARegulatedDevice']
    phase = study['DesignModule']['PhaseList']['Phase']
    sponsor = study['SponsorCollaboratorsModule']['LeadSponsor']['LeadSponsorName']

    if (isFDARegulatedDevice == 'Yes' or isFDARegulatedDrug == 'Yes'):
        print(nctId + ' | ' + orgStudyId  + ' | ' + orgFullName + ' | ' + primaryCompletionDate) 


path = 'C:\\Users\\tcurek\Desktop\\FDA'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files[:10]:
    read_file(f)
