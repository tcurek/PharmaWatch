import json
import os

def read_file(path):
    with open(path, 'r', encoding='utf8', errors='ignore') as json_file:
        data = json.load(json_file)

    study = data['FullStudy']['Study']
    protocol_selection = study['ProtocolSection']
    identification_module = protocol_selection['IdentificationModule']
    oversight =  study.get('OversightModule',{'OversightHasDMC':'No','IsFDARegulatedDrug':'No','IsFDARegulatedDevice':'No'})

    # data
    nctId = identification_module['NCTId']
    orgStudyId = identification_module['OrgStudyIdInfo']['OrgStudyId']
    orgFullName = protocol_selection.get('Organization', {'OrgFullName': 'N/A'})['OrgFullName']
    overallStatus = study.get('StatusModule', {'OverallStatus':'N/A'})['OverallStatus']
    startDate = study['StartDateStruct']['StartDate']
    primaryCompletionDate = study['PrimaryCompletionDateStruct']['PrimaryCompletionDate']
    completionDate = study['CompletionDateStruct']['CompletionDate']
    isFDARegulatedDrug = oversight['IsFDARegulatedDrug']
    isFDARegulatedDevice = oversight['IsFDARegulatedDevice']
    phase = study['DesignModule']['PhaseList']['Phase']
    sponsor = study['SponsorCollaboratorsModule']['LeadSponsor']['LeadSponsorName']

    print(path + ' | ' + nctId + ' | ' + orgStudyId  + ' | ' + orgFullName + ' | ' + primaryCompletionDate + ' | ' + isFDARegulatedDevice + ' | ' +  isFDARegulatedDrug) 


path = 'C:\\Users\\tcurek\Desktop\\FDA'

number_of_files = 0

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))
            number_of_files += 1

print('Starting...')
print('Found ' + str(number_of_files) + ' files.')

for f in files:
    read_file(f)

print('Finished...')