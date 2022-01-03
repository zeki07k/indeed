# import lxml
#
# a = """<div id="jobDescriptionText" class="jobsearch-jobDescriptionText"><div><div><div><ul><div><div><b>Job Summary</b></div>\n<ul><div><div>The incumbent in this position provides patients, families of patients, v
# isitors, and medical center employees with a pleasant, comfortable, safe, functional, and aesthetically attractive environment consistent with the standards established by Georgetown University Hospital, the D
# istrict of Columbia Department of Consumer and Regulatory Affairs (DCRA), and the Joint Commission on Accreditation of Health care Organizations (THE JOINT COMMISSION). In this position the incumbent performs
# various housekeeping and heavy-duty cleaning throughout all Hospital buildings and surrounding areas and inventories and distributes linen supplies and equipment to user units. The incumbent also maintains eff
# ective communications and working relationships with customers. These functions are performed in accordance with all applicable laws and regulations and MedStar Georgetown University Hospital’s philosophy, pol
# icies, procedures and standards.</div>\n</div></ul></div><div><div><b>Minimum Qualifications</b></div>\n<ul><div><div><b>CONSIDERATION WILL BE GIVEN TO AN APPROPRIATE COMBINATION OF EDUCATION/TRAINING AND EXPE
# RIENCE.</b></div>\n</div><div></div><div><div><b>Education/Training</b></div>\n<ul><li><div>High school diploma or GED preferred.</div>\n</li></ul></div><div></div><div><div><b>Experience</b></div>\n<ul><li><d
# iv>No prior experience required.</div>\n</li></ul></div><div></div><div><div><b>License/Certification/Registration</b></div>\n<ul><li><div>N/A</div>\n</li></ul></div><div></div><div><div><b>Knowledge, Skills &
# amp; Abilities</b></div>\n<ul><li><div>Should be able to read, write and speak English. Ability to follow oral and written instructions. Ability to learn occupational hazards and the safety precautions of the
# job and the application of universal (isolation) precautions for patients. As a key representative of Georgetown University Hospital, must have effective communication and interpersonal skills to relate to sta
# ff, visitors and patients with varying degrees of illness. Ability to set priorities and meet deadlines. Must be flexible in order to function in a setting which may be stressful or change unexpectedly due to
# a patient’s condition. Must Be Customer Focused with A Service Attitude.</div>\n</li></ul></div></ul></div><div><div><b>Primary Duties and Responsibilities</b></div>\n<ul><li><div>Maintains a pleasant and coop
# erative service attitude towards patients, families of patients, visitors, medical center staff, co-workers and management at all-times while working as part of a team maintaining a healing patient environment
# .</div>\n</li><li><div>Performs thorough daily cleaning in assigned areas, following established schedules and using prescribed procedures. Tasks include but not limited to: Performance of a 10 STEP CLEANING p
# rocess (Knock and Greet patient/family, Empty waste, High Dust, Sanitize, Spot Clean, Restroom, Dust mop the floor, Inspect the room, Damp Mop the floor, Interact with the patient/family).</div>\n</li><li><div
# >High dust all above shoulder surfaces and ceiling vents/lights. Damp wipes all ledges, furnishings, furniture, lights, shelves, light switches, telephones, door knobs, et cetera. Spot clean walls, doors and w
# indows/glass. Clean and disinfect bathrooms/restrooms to include sinks, toilets, showers, tubes, floors, pipes, mirrors, urinals, etc and restock disposable items such as soap, toilet paper, seat covers, and p
# aper towels. Dust mop floors using a chemically treated mop. Vacuum carpeted floors and upholstery. Remove spots from carpet. Damp mop floors using prescribed cleaning agents. Inspect your work and report main
# tenance needs in patient rooms, exam/treatment rooms, restrooms, offices, labs, departments, public areas and ancillary areas.</div>\n</li><li><div>Performs check-out/transfer cleaning in assigned area and/or
# as assigned by supervision which includes utilizing the above 10-Step Cleaning in addition to stripping, cleaning and remaking beds; removing all patient supplies and equipment; and proper room setup.</div>\n<
# /li><li><div>Performs Between-Case-Cleaning in Labor &amp; Delivery and the main Operating Room: Terminal Cleaning in Labor &amp; Delivery and the Operating Room.</div>\n</li><li><div>Washes ceiling surfaces;
# cleaning of elevators and stairwells; cleaning parking lots, garages, entrances and sweeping sidewalks; washing interior windows; defrosting and cleaning refrigerators.</div>\n</li><li><div>Takes down and reha
# ngs drapes, showers curtains and cubical curtains; Transports trash in bulk trash carts to the back dock, prepares medical waste trash and operates the compactor equipment; Uses mechanical cleaning equipment t
# o maintain cleanliness and appearance of hard surfaces floors and carpets which may include stripping, finishing, buffing/burnishing, sweeping, vacuuming, dust mopping, damp mopping, shampooing, bonnet cleanin
# g, extracting and carpet spotting.</div>\n</li><li><div>Moves and/or assists in moving of furniture for setting up/breaking down conference/classrooms;</div>\n</li><li><div>Conducts general daily inspections o
# f all assigned areas and makes initial assessment of problems in the environment (malfunction beds, furniture, equipment, plumbing, walls, ceilings, etc) and reports identified problems to service center.</div
# >\n</li><li><div>Utilizes a wide variety of institutional and industrial cleaning and maintenance chemicals and power equipment according to departmental and OSHA regulations.</div>\n</li><li><div>Completes sc
# heduled and assigned tasks under normal conditions within prescribed time parameters with accuracy and consistency.</div>\n</li><li><div>Presents a professional image at all times as demonstrated by a high deg
# ree of integrity, technical knowledge, personal appearance (neat, clean, in uniform and wears name tag), equipment/work space orderliness/cleanliness and service attitude.</div>\n</li><li><div>Makes effective
# use of departmental/medical center resources (time, material, equipment, etc) so as to minimize waste and prevent damage.</div>\n</li><li><div>Demonstrates a constant awareness of unsafe or potentially unsafe
# working conditions and makes every effort to correct and report hazards to the proper authority. Accepts responsibility for ensuring the working environment is safe and in good repair, and places the appropria
# te work orders with supervisor or directly with facilities to ensure appropriate maintenance of environment. Knows and responds appropriately to safety, fire and disaster procedures.</div>\n</li><li><div>Demon
# strates initiative in job performance through suggesting methods/procedures to improve quality, service, productivity, and efficiency and willingness to accept and support change.</div>\n</li><li><div>Utilizes
#  ESD equipment to ensure appropriate cleaning for our clients. Maintains equipment and ensure appropriate use of said equipment.</div>\n</li><li><div>Pursues self development through attendance at and active p
# articipation in Department/Medical Center training sessions and meetings. Participates in appropriate committees as assigned.</div>\n</li><li><div>Completes all required annual education requirements thru Geor
# getown University Hospital resources.</div>\n</li><li><div>Works cooperatively with other medical center departments such as Nursing, Maintenance, Materials Management, etc and coordinates with to provide serv
# ices to customers.</div>\n</li><li><div>Maintains a good work attendance and punctuality record in accordance with department policies.</div>\n</li><li><div>Performs other duties and responsibilities that are
# appropriate to the position and area. The above responsibilities are a general description of the level and nature of the work assigned to this classification and is not to be considered as all inclusive.</div
# ></li></ul></div></ul></div></div></div></div>
# """



import re
# pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)
# text = pattern.sub(" ", a)
#
# b = re.sub('<[^<]+?>', '', a)

a ='https://www.indeed.com/viewjob?jk=47ae1fc984b48af7'

b = re.sub('\?(.*)', '',a)
c = re.sub('[^\s.](?:[^?.]|\.(?! ))*\?','',a)
print(c)