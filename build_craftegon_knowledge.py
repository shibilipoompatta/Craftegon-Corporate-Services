"""
build_craftegon_knowledge.py
Generates the authoritative, original legal compliance and procedure guides for
CraftEgon Corporate Services into data/craftegon-knowledge-hub.json.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

GUIDES = [
    {
        "guide_id": "pvt-ltd-incorporation-guide",
        "related_service_id": "private-limited-company-incorporation",
        "title": "Private Limited Company Incorporation: Complete 2026 Legal & MCA V3 Manual",
        "slug": "pvt-ltd-incorporation-guide",
        "category": "business-setup",
        "meta_description": "Comprehensive guide to Private Limited Company incorporation in India under Companies Act 2013, SPICe+ MCA V3 portal, required documents, stamp duties, and compliance checklists.",
        "read_time": "7 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "A Private Limited Company is the most credible and scalable corporate structure in India for startups, growing SMEs, and enterprise ventures seeking equity funding and limited liability protection under the Companies Act, 2013.",
            "eligibility": [
                "Minimum of two directors and two shareholders (promoters can hold both roles).",
                "At least one director must be a permanent resident of India (stayed > 182 days in India in the previous FY).",
                "No minimum statutory capital requirement (can be started with as low as ₹1,000 to ₹1 Lakh).",
                "Unique commercial name adhering strictly to the Companies (Incorporation) Rules, 2014.",
                "Valid residential and registered commercial office address proof situated within India."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Digital Signature Certificate (DSC Class 3)",
                    "detail": "Obtain Class 3 Digital Signature Certificates with crypto tokens for all designated directors to legally sign MCA electronic forms."
                },
                {
                    "step": 2,
                    "title": "RUN Name Approval (SPICe+ Part A)",
                    "detail": "Submit up to two unique company names on the MCA V3 portal via SPICe+ Part A. Name must reflect business activity and end with 'Private Limited'."
                },
                {
                    "step": 3,
                    "title": "SPICe+ Part B & Integrated Registrations",
                    "detail": "Draft e-MOA (INC-33), e-AOA (INC-34), and file Part B covering DIN allotment, PAN, TAN, EPFO, ESIC, Professional Tax, and mandatory bank account opening."
                },
                {
                    "step": 4,
                    "title": "Certificate of Incorporation (COI)",
                    "detail": "The Registrar of Companies (ROC) audits documents and issues the digitally signed Certificate of Incorporation containing CIN, PAN, and TAN."
                },
                {
                    "step": 5,
                    "title": "Bank Account & INC-20A Commencement Filing",
                    "detail": "Deposit subscription money into the corporate bank account within 180 days and file Form INC-20A before starting commercial operations."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Within 30 Days", "compliance": "First Board Meeting & Appointment of Statutory Auditor (Form ADT-1)"},
                {"timeline": "Within 180 Days", "compliance": "Filing of Declaration of Commencement of Business (Form INC-20A)"},
                {"timeline": "Annual (By Sept 30)", "compliance": "Annual General Meeting (AGM) and Director KYC (DIR-3 KYC)"},
                {"timeline": "Within 30 Days of AGM", "compliance": "Filing of Balance Sheet & P&L (Form AOC-4)"},
                {"timeline": "Within 60 Days of AGM", "compliance": "Filing of Annual Return (Form MGT-7/7A)"}
            ],
            "required_documents": [
                "PAN Card of all Directors and Shareholders",
                "Identity Proof: Aadhaar Card, Passport, or Voter ID",
                "Address Proof: Latest Bank Statement, Electricity Bill, or Mobile Bill (< 2 months old)",
                "Passport Size Photographs of all Directors",
                "Registered Office Proof: Electricity Bill or Property Tax Receipt (< 2 months old)",
                "No Objection Certificate (NOC) signed by the property owner",
                "Rent / Lease Agreement executed on non-judicial stamp paper"
            ]
        },
        "faqs": [
            {
                "question": "Can a foreign national or NRI be a director in an Indian Private Limited Company?",
                "answer": "Yes. Foreign nationals and NRIs can become directors and shareholders, provided at least one director on the board is a resident Indian. Foreign KYC documents must be notarized or apostilled in the home country."
            },
            {
                "question": "What is the government fee for incorporating a company with ₹10 Lakhs capital?",
                "answer": "Under the Zero MCA Fee initiative, MCA charges ₹0 ROC filing fee for authorized capital up to ₹15 Lakhs. Only state-specific stamp duty on MOA, AOA, and SPICe+ form is payable."
            },
            {
                "question": "Is a commercial office mandatory for registered office address?",
                "answer": "No. A residential property can also be declared as the registered office of the company, provided a utility bill and owner NOC are furnished."
            },
            {
                "question": "How long does the entire incorporation process take?",
                "answer": "Typically between 5 to 7 working days, subject to MCA V3 portal processing and ROC approval speed."
            }
        ]
    },
    {
        "guide_id": "llp-incorporation-guide",
        "related_service_id": "limited-liability-partnership-llp",
        "title": "Limited Liability Partnership (LLP) Registration: Complete Procedure & Compliance",
        "slug": "llp-incorporation-guide",
        "category": "business-setup",
        "meta_description": "Comprehensive legal manual on Limited Liability Partnership (LLP) formation in India under LLP Act 2008, FiLLiP MCA V3 portal filings, and LLP Agreement drafting.",
        "read_time": "6 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "A Limited Liability Partnership (LLP) combines the operational flexibility of a traditional partnership firm with the limited liability shield and corporate identity of a joint stock company, governed by the LLP Act, 2008.",
            "eligibility": [
                "Minimum of two designated partners (individuals or corporate bodies).",
                "At least one designated partner must be an Indian resident.",
                "Every designated partner must possess a valid Designated Partner Identification Number (DPIN/DIN).",
                "Digital Signature Certificate (DSC Class 3) for authorized signatories."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "RUN-LLP Name Reservation",
                    "detail": "Reserve up to two proposed LLP names on the MCA V3 portal using the RUN-LLP electronic application."
                },
                {
                    "step": 2,
                    "title": "FiLLiP Form Submission",
                    "detail": "Submit Form FiLLiP (Form for Incorporation of Limited Liability Partnership) with partner details, address proof, and DPIN applications."
                },
                {
                    "step": 3,
                    "title": "Certificate of Incorporation",
                    "detail": "ROC reviews and issues the digital Certificate of Incorporation with a unique 7-digit LLP Identification Number (LLPIN)."
                },
                {
                    "step": 4,
                    "title": "LLP Agreement Execution & Form 3",
                    "detail": "Draft, print on state stamp paper, execute, and file the LLP Agreement within 30 days of incorporation using Form 3."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Within 30 Days of Incorporation", "compliance": "Filing of Executed LLP Agreement (Form 3)"},
                {"timeline": "Annually by May 30", "compliance": "Filing of Statement of Solvency & Annual Accounts (Form 11)"},
                {"timeline": "Annually by October 30", "compliance": "Filing of Statement of Account & Solvency (Form 8)"},
                {"timeline": "Annually by July 31 / Oct 31", "compliance": "Filing of Income Tax Return (ITR-5)"}
            ],
            "required_documents": [
                "PAN Card of all Designated Partners",
                "Aadhaar Card / Passport / Voter ID",
                "Bank Statement or Utility Bill (< 2 months old)",
                "Registered Office proof (Electricity bill + Owner NOC + Rental deed)",
                "Partnership Capital Contribution statement"
            ]
        },
        "faqs": [
            {
                "question": "Is statutory audit mandatory for all LLPs every year?",
                "answer": "No. An LLP requires statutory audit only if its annual turnover exceeds ₹40 Lakhs or if its total capital contribution exceeds ₹25 Lakhs."
            },
            {
                "question": "Can an existing partnership firm convert into an LLP?",
                "answer": "Yes. A partnership firm can convert into an LLP under Section 55 and Chapter X of the LLP Act, 2008 by filing Form 17."
            }
        ]
    },
    {
        "guide_id": "gst-registration-guide",
        "related_service_id": "gst-registration",
        "title": "GST Registration in India: Thresholds, Verification & Online Application Guide",
        "slug": "gst-registration-guide",
        "category": "gst-advisory",
        "meta_description": "Authoritative guide on GST registration in India under CGST Act 2017: aggregate turnover limits, Aadhaar authentication, documents required, and TRN generation.",
        "read_time": "6 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Goods and Services Tax (GST) registration is a mandatory 15-digit tax identification number (GSTIN) issued by the Central Board of Indirect Taxes and Customs (CBIC) for businesses supplying goods or services exceeding statutory turnover thresholds.",
            "eligibility": [
                "Goods Suppliers: Aggregate annual turnover exceeding ₹40 Lakhs (₹20 Lakhs for Special Category States).",
                "Service Providers: Aggregate annual turnover exceeding ₹20 Lakhs (₹10 Lakhs for Special Category States).",
                "Interstate Taxable Suppliers: Mandatory registration irrespective of turnover threshold.",
                "E-Commerce Sellers & Operators: Mandatory registration under Section 24 of CGST Act.",
                "Casual Taxable Persons & Non-Resident Taxable Persons."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "TRN Generation (Part A of REG-01)",
                    "detail": "Enter PAN, mobile number, and email ID on the GST common portal to receive OTPs and generate a Temporary Reference Number (TRN)."
                },
                {
                    "step": 2,
                    "title": "Form REG-01 (Part B) Submission",
                    "detail": "Complete business details, principal place of business, bank account information, HSN/SAC codes, and upload proof of business premises."
                },
                {
                    "step": 3,
                    "title": "Aadhaar Authentication",
                    "detail": "Promoter and primary authorized signatory complete biometric or OTP-based Aadhaar authentication for instant deemed approval within 7 working days."
                },
                {
                    "step": 4,
                    "title": "GSTIN & Certificate Issuance (REG-06)",
                    "detail": "Upon verification, Form GST REG-06 is generated with the 15-digit alphanumeric GSTIN."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Monthly (By 11th)", "compliance": "Filing of Outward Supplies (Form GSTR-1)"},
                {"timeline": "Monthly (By 20th)", "compliance": "Summary Return & Net Tax Settlement (Form GSTR-3B)"},
                {"timeline": "Quarterly (QRMP)", "compliance": "Invoice Furnishing Facility (IFF) and Quarterly GSTR-3B"},
                {"timeline": "Annually (By Dec 31)", "compliance": "Filing of GST Annual Return (Form GSTR-9)"}
            ],
            "required_documents": [
                "PAN Card of the Business / Proprietor",
                "Aadhaar Card and Photograph of Promoters",
                "Proof of Business Registration (COI / Partnership Deed / Trade License)",
                "Proof of Principal Place of Business (Electricity bill, Property Tax receipt, Rent agreement & Owner NOC)",
                "Bank Account Proof (Cancelled cheque, Passbook first page, or Bank statement)"
            ]
        },
        "faqs": [
            {
                "question": "Can I obtain voluntary GST registration before reaching the ₹40 Lakh threshold?",
                "answer": "Yes. Any business entity can voluntarily register under Section 25(3) of the CGST Act to claim Input Tax Credit (ITC) and sell to B2B clients."
            },
            {
                "question": "What happens if Aadhaar authentication fails or is opted out?",
                "answer": "If Aadhaar authentication is skipped, the GST officer conducts physical site verification or requests additional document clarification within 30 days."
            }
        ]
    },
    {
        "guide_id": "gst-return-filing-guide",
        "related_service_id": "gst-return-filing-gstr-1-3b",
        "title": "GSTR-1 & GSTR-3B Return Filing: Due Dates, Penalties & Reconciliation Guide",
        "slug": "gst-return-filing-guide",
        "category": "gst-advisory",
        "meta_description": "Complete breakdown of periodic GST return filing for Indian businesses: GSTR-1, GSTR-3B, GSTR-2B reconciliation, input tax credit rules under Section 16, and late fee formulas.",
        "read_time": "5 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Every registered GST taxpayer must regularly file outward sales statements and summary tax settlements. Accurate filing prevents cancellation of GSTIN and preserves business buyer relationships by ensuring timely ITC reflection in GSTR-2B.",
            "eligibility": [
                "All active regular GSTIN holders.",
                "Composition dealers file quarterly CMP-08 and annual GSTR-4.",
                "Nil return filers must file Nil returns via SMS or web portal."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Invoice Ledger Compilation",
                    "detail": "Collate all B2B tax invoices, credit/debit notes, B2C sales summaries, and export shipping bills."
                },
                {
                    "step": 2,
                    "title": "GSTR-1 Upload & Validation",
                    "detail": "Upload invoice data to GST portal, verify HSN summary, validate taxable values, and file with DSC or EVC."
                },
                {
                    "step": 3,
                    "title": "GSTR-2B Auto-Drafted ITC Reconciliation",
                    "detail": "Compare purchase register against GSTR-2B generated on the 14th of each month to claim eligible Input Tax Credit."
                },
                {
                    "step": 4,
                    "title": "GSTR-3B Tax Offset & Payment",
                    "detail": "Offset output liabilities against available ITC, pay remaining tax through electronic cash ledger, and submit the return."
                }
            ],
            "compliance_checklist": [
                {"timeline": "11th of Every Month", "compliance": "Monthly GSTR-1 Filing Due Date"},
                {"timeline": "13th of Month Following Quarter", "compliance": "QRMP GSTR-1 Filing Due Date"},
                {"timeline": "20th of Every Month", "compliance": "Monthly GSTR-3B Filing & Tax Payment"},
                {"timeline": "22nd / 24th of Month Following Quarter", "compliance": "QRMP GSTR-3B (Staggered by State)"}
            ],
            "required_documents": [
                "Sales Invoices Register with GSTIN, HSN, Taxable Value, CGST/SGST/IGST",
                "Purchase Register / Bill of Entry for Imports",
                "Expense Bills attracting Reverse Charge Mechanism (RCM)",
                "Bank Statement for reconciliation of tax debits"
            ]
        },
        "faqs": [
            {
                "question": "What is the late fee for delayed GSTR-3B filing?",
                "answer": "For Nil returns: ₹20 per day (₹10 CGST + ₹10 SGST). For returns with tax liability: ₹50 per day (₹25 CGST + ₹25 SGST), subject to statutory caps based on turnover."
            },
            {
                "question": "Can I claim ITC on invoices that do not appear in GSTR-2B?",
                "answer": "No. Under Section 16(2)(aa) of the CGST Act, 100% matching with GSTR-2B is strictly mandatory before claiming Input Tax Credit."
            }
        ]
    },
    {
        "guide_id": "trademark-registration-guide",
        "related_service_id": "trademark-registration",
        "title": "Trademark Registration in India: Nice Classification, Search & Legal Process",
        "slug": "trademark-registration-guide",
        "category": "brand-protection",
        "meta_description": "Comprehensive guide to trademark registration in India under Trademarks Act 1999: TM search, Class 1 to 45 classification, Form TM-A, examination reports, and journal publication.",
        "read_time": "7 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "A registered trademark grants 10 years of statutory brand protection under the Trade Marks Act, 1999, providing exclusive proprietary rights to brand names, logos, slogans, and sounds across 45 Nice Classification classes.",
            "eligibility": [
                "Individuals, Sole Proprietorships, Startups, LLPs, Private Limited, and Public Limited Companies.",
                "Non-governmental organizations, trusts, and foreign entities.",
                "Marks that are distinctive, non-descriptive, and not phonetically or visually deceptively similar to earlier marks."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Comprehensive Trademark Search",
                    "detail": "Search IP India public database to verify that the mark is distinctive and has no prior conflicting registrations or pending applications."
                },
                {
                    "step": 2,
                    "title": "Class Selection & TM-A Filing",
                    "detail": "Select proper classes (Goods: Class 1-34, Services: Class 35-45) and electronically file Form TM-A with IP India portal."
                },
                {
                    "step": 3,
                    "title": "Examination Report Review",
                    "detail": "The Trade Marks Registry examines the mark under Section 9 (absolute grounds) and Section 11 (relative grounds) within 1 to 3 months."
                },
                {
                    "step": 4,
                    "title": "Publication in Trade Marks Journal",
                    "detail": "If accepted, the mark is advertised in the official Trade Marks Journal for a statutory 4-month public opposition period."
                },
                {
                    "step": 5,
                    "title": "Registration Certificate Issuance",
                    "detail": "If no opposition is filed or opposition is decided in your favor, the Registrar issues the Digital Registration Certificate (granting ® rights)."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Immediate on Filing", "compliance": "Lawful right to use the ™ symbol alongside your brand"},
                {"timeline": "Within 30 Days of Exam Report", "compliance": "Mandatory reply to Trademark Examination Report / Objection"},
                {"timeline": "Every 10 Years", "compliance": "Renewal of Registered Trademark (Form TM-R)"}
            ],
            "required_documents": [
                "Logo / Brand Artwork in clean high-resolution format",
                "Applicant Identity Proof (PAN & Aadhaar / COI)",
                "Power of Attorney / Authorization Form TM-48",
                "User Affidavit with documentary proof of prior usage (if mark is already in use)"
            ]
        },
        "faqs": [
            {
                "question": "What is the difference between ™ and ® symbols?",
                "answer": "™ denotes that a trademark application has been filed and is pending. ® can strictly and legally only be used after the Registrar issues the final Registration Certificate."
            },
            {
                "question": "What is the government fee for filing Form TM-A?",
                "answer": "Government fee is ₹4,500 per class for Individuals, Startups (DPIIT recognized), and MSMEs. For corporate entities without MSME, the fee is ₹9,000 per class."
            }
        ]
    },
    {
        "guide_id": "trademark-objection-reply-guide",
        "related_service_id": "trademark-objection-reply",
        "title": "Trademark Objection Reply: Section 9 & 11 Legal Defense Strategy",
        "slug": "trademark-objection-reply-guide",
        "category": "brand-protection",
        "meta_description": "Legal strategy guide for drafting persuasive replies to Trademark Examination Reports under Section 9 (Absolute Grounds) and Section 11 (Relative Grounds) of Trade Marks Act 1999.",
        "read_time": "6 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Over 70% of trademark applications in India encounter Examination Objections from the Trademark Registry. Submitting a robust, precedent-backed legal reply within the statutory 30-day window is essential to avoid application abandonment.",
            "eligibility": [
                "Any applicant who has received an Examination Report with status 'Objected'."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Analyze Grounds of Objection",
                    "detail": "Determine whether objection is raised under Section 9 (lack of distinctive character/descriptive terms) or Section 11 (conflict with existing registered mark)."
                },
                {
                    "step": 2,
                    "title": "Gather Evidence of Secondary Meaning",
                    "detail": "Assemble invoices, advertisement copies, turnover figures, domain registration dates, and social media traction establishing acquired distinctiveness."
                },
                {
                    "step": 3,
                    "title": "Draft Substantive Legal Reply",
                    "detail": "Draft legal response citing relevant high court and supreme court IP precedents, highlighting phonetic, visual, and conceptual distinctions."
                },
                {
                    "step": 4,
                    "title": "Online Submission via Comprehensive e-Filing",
                    "detail": "Submit the response along with supporting exhibits and user affidavit on the official IP India portal."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Strict 30-Day Window", "compliance": "Filing formal reply from date of receipt of Examination Report"},
                {"timeline": "Post Reply", "compliance": "Monitoring portal for acceptance or scheduling of Show Cause Hearing"}
            ],
            "required_documents": [
                "Copy of Official Examination Report",
                "Executed Form TM-48 (Power of Attorney)",
                "Affidavit of Evidence with historical commercial invoices showing brand use",
                "Domain whois records, marketing brochures, and audited sales certificates"
            ]
        },
        "faqs": [
            {
                "question": "What happens if I miss the 30-day deadline to reply to the examination report?",
                "answer": "If you fail to reply within 30 days (or file an extension under Form TM-M), the Registrar will mark the application as 'Abandoned'."
            }
        ]
    },
    {
        "guide_id": "fssai-food-license-guide",
        "related_service_id": "fssai-registration",
        "title": "FSSAI Food Business License: Registration vs State vs Central License Guide",
        "slug": "fssai-food-license-guide",
        "category": "business-setup",
        "meta_description": "Comprehensive manual on FSSAI Food Safety Registration and Licensing in India under Food Safety and Standards Act 2006: FoSCoS portal filings, eligibility slabs, and annual compliance.",
        "read_time": "6 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Every Food Business Operator (FBO) involved in manufacturing, processing, storage, distribution, packaging, or sale of food products must mandatorily hold an FSSAI 14-digit license or registration under the FSS Act, 2006.",
            "eligibility": [
                "Basic Registration: Annual turnover up to ₹12 Lakhs (Petty food manufacturers, hawkers, small retailers).",
                "State License: Annual turnover between ₹12 Lakhs and ₹20 Crores (Medium restaurants, cloud kitchens, manufacturers).",
                "Central License: Annual turnover exceeding ₹20 Crores, or operating in 100% export/import, e-commerce, or multi-state chains."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "FoSCoS Portal Account Creation",
                    "detail": "Register on the Food Safety Compliance System (FoSCoS) portal and select relevant Kind of Business (KoB)."
                },
                {
                    "step": 2,
                    "title": "Form A (Registration) / Form B (License) Filing",
                    "detail": "Fill facility layout, production capacity, food product categories, and technical personnel credentials."
                },
                {
                    "step": 3,
                    "title": "Food Safety Management System (FSMS) & Documents",
                    "detail": "Upload water test reports, equipment list, FSMS plan, layout blueprint, and premises ownership proof."
                },
                {
                    "step": 4,
                    "title": "Physical Inspection & Grant of 14-Digit License",
                    "detail": "Food Safety Officer (FSO) verifies the premise hygiene; upon satisfaction, the digital 14-digit FSSAI License is issued."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Annual (By May 31)", "compliance": "Filing of Annual Return (Form D-1) on FoSCoS"},
                {"timeline": "Periodic (Every 6 Months)", "compliance": "Water Test Report & Food Safety Audit by NABL accredited lab"},
                {"timeline": "Before Expiry (1-5 Years)", "compliance": "FSSAI License Renewal (at least 30 days before validity ends)"}
            ],
            "required_documents": [
                "Photo ID and Address Proof of Proprietor/Directors",
                "Proof of Possession of Premises (Rental Deed + Utility Bill + NOC)",
                "Partnership Deed / Certificate of Incorporation",
                "List of Food Products and Categories intended to be handled",
                "Layout Plan of processing unit with dimensions (for manufacturing/processing)",
                "Water Analysis Test Report from recognized laboratory"
            ]
        },
        "faqs": [
            {
                "question": "Can I operate a home-based cloud kitchen with basic FSSAI registration?",
                "answer": "Yes. Home kitchens and small food startups with annual revenue under ₹12 Lakhs can start operations legally with a Basic FSSAI Registration."
            }
        ]
    },
    {
        "guide_id": "msme-udyam-registration-guide",
        "related_service_id": "udyam-registration",
        "title": "MSME Udyam Registration: Classification Slabs, Subsidies & Benefits",
        "slug": "msme-udyam-registration-guide",
        "category": "business-setup",
        "meta_description": "Guide to MSME Udyam registration in India: revised Composite Criteria for Micro, Small, and Medium enterprises, collateral-free loans, priority sector lending, and patent rebates.",
        "read_time": "5 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Udyam Registration is the government's official recognition portal for Micro, Small, and Medium Enterprises in India, providing access to public procurement priorities, interest rate subventions, and statutory protection against delayed payments.",
            "eligibility": [
                "Micro Enterprise: Investment in Plant & Machinery <= ₹1 Crore AND Annual Turnover <= ₹5 Crores.",
                "Small Enterprise: Investment <= ₹10 Crores AND Annual Turnover <= ₹50 Crores.",
                "Medium Enterprise: Investment <= ₹50 Crores AND Annual Turnover <= ₹250 Crores."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Aadhaar & PAN Verification",
                    "detail": "Enter 12-digit Aadhaar number of entrepreneur or authorized signatory on the official Udyam portal."
                },
                {
                    "step": 2,
                    "title": "Automated Income Tax & GST Data Sync",
                    "detail": "Portal automatically retrieves investment and turnover figures directly from Income Tax and GSTN servers."
                },
                {
                    "step": 3,
                    "title": "Enterprise Information Submission",
                    "detail": "Enter National Industry Classification (NIC) 2-digit and 5-digit codes for core manufacturing or service operations."
                },
                {
                    "step": 4,
                    "title": "Instant Udyam Registration Certificate",
                    "detail": "The system instantly generates the permanent Udyam Registration Certificate featuring a verifiable dynamic QR code."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Annual Update", "compliance": "Annual filing of ITR and GST return automatically updates classification"},
                {"timeline": "Within 45 Days", "compliance": "Statutory right to receive payment from corporate buyers under Section 15 of MSMED Act"}
            ],
            "required_documents": [
                "Aadhaar Card of the Proprietor / Managing Partner / Director",
                "PAN Card of the Business or Proprietor",
                "Bank Account Details (Account Number & IFSC Code)",
                "GSTIN (if GST is registered)"
            ]
        },
        "faqs": [
            {
                "question": "Is there any government fee for Udyam Registration?",
                "answer": "No. The Government of India charges zero statutory fee for issuing an Udyam Certificate."
            },
            {
                "question": "What is the protection against delayed payments for MSMEs?",
                "answer": "Under the MSMED Act, buyers must pay MSME suppliers within 45 days. Delayed payments attract compounding interest at three times the RBI bank rate."
            }
        ]
    },
    {
        "guide_id": "annual-roc-filing-guide",
        "related_service_id": "annual-filing-roc-compliance",
        "title": "Annual MCA ROC Compliance: AOC-4, MGT-7, DIR-3 KYC & Penalties Manual",
        "slug": "annual-roc-filing-guide",
        "category": "corporate-governance",
        "meta_description": "Complete corporate compliance manual for Private Limited and Public Limited companies: AOC-4, MGT-7, statutory audit, Board Report, and DIR-3 KYC filing rules.",
        "read_time": "7 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Every company incorporated in India is legally mandated under the Companies Act, 2013 to file annual financial statements and return of shareholders with the Registrar of Companies (ROC), even if the company has zero transactions during the fiscal year.",
            "eligibility": [
                "All Private Limited Companies, OPCs, Section 8 companies, and Public Limited Companies."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Statutory Financial Audit",
                    "detail": "Independent Chartered Accountant audits company books and signs Audit Report with CARO (where applicable)."
                },
                {
                    "step": 2,
                    "title": "Board of Directors Meeting & Board's Report",
                    "detail": "Convene Board Meeting to approve financial statements and draft the statutory Board's Report under Section 134."
                },
                {
                    "step": 3,
                    "title": "Annual General Meeting (AGM)",
                    "detail": "Conduct AGM within 6 months of financial year end (on or before September 30) to adopt accounts."
                },
                {
                    "step": 4,
                    "title": "Form AOC-4 Submission",
                    "detail": "File Balance Sheet, Profit & Loss statement, Auditor Report, and Notes to Accounts within 30 days of AGM."
                },
                {
                    "step": 5,
                    "title": "Form MGT-7 / MGT-7A Submission",
                    "detail": "File Annual Return detailing shareholding pattern, board meetings, and director remuneration within 60 days of AGM."
                }
            ],
            "compliance_checklist": [
                {"timeline": "By September 30", "compliance": "Director Annual KYC (Form DIR-3 KYC / Web-KYC)"},
                {"timeline": "Within 30 Days of AGM", "compliance": "Filing of Financial Statements (Form AOC-4)"},
                {"timeline": "Within 60 Days of AGM", "compliance": "Filing of Annual Return (Form MGT-7 / MGT-7A for small companies)"},
                {"timeline": "Half-Yearly (MSME-1)", "compliance": "Reporting of Outstanding Dues to Micro & Small Enterprises"}
            ],
            "required_documents": [
                "Audited Balance Sheet & Profit and Loss Statement with schedules",
                "Independent Statutory Auditor's Report",
                "Director's Report with required disclosures",
                "Notice of AGM, List of Shareholders, and Share Transfer Register",
                "Digital Signature Certificates (DSC) of Director and practicing CA/CS"
            ]
        },
        "faqs": [
            {
                "question": "What is the penalty for delayed AOC-4 and MGT-7 filings?",
                "answer": "MCA levies a severe recurring late fee of ₹100 per day per form with no upper ceiling. Persistent default can lead to director disqualification and company strike-off."
            }
        ]
    },
    {
        "guide_id": "corporate-itr-tax-audit-guide",
        "related_service_id": "corporate-income-tax-filing",
        "title": "Corporate Income Tax (ITR-6) & Tax Audit (Form 3CD): Deadlines & Slabs",
        "slug": "corporate-itr-tax-audit-guide",
        "category": "direct-tax",
        "meta_description": "Comprehensive corporate tax guide: filing Form ITR-6, Section 44AB tax audit thresholds, Form 3CA/3CB/3CD, Section 115BAA concessional 22% tax regime, and MAT compliance.",
        "read_time": "6 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "Corporate Income Tax compliance requires Indian companies to compute taxable profits under the Income Tax Act, 1961, claim allowable depreciation and deductions, and file Form ITR-6 alongside mandatory Tax Audit Reports.",
            "eligibility": [
                "All domestic and foreign companies registered in India.",
                "Tax Audit is mandatory if business turnover exceeds ₹10 Crores (provided digital transactions exceed 95%) or ₹1 Crore (for cash businesses)."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Advance Tax Computation & Payment",
                    "detail": "Estimate annual corporate profits and pay advance tax in 4 quarterly installments (June 15, Sept 15, Dec 15, March 15)."
                },
                {
                    "step": 2,
                    "title": "Statutory Tax Audit (Section 44AB)",
                    "detail": "Independent Chartered Accountant conducts tax audit and electronically uploads Form 3CA/3CD on the e-filing portal."
                },
                {
                    "step": 3,
                    "title": "Tax Audit Approval by Assessee",
                    "detail": "Director reviews and approves the submitted Form 3CD on the portal using corporate DSC."
                },
                {
                    "step": 4,
                    "title": "ITR-6 Computation & Filing",
                    "detail": "Prepare JSON utility for Form ITR-6, reconcile with AIS/TIS, pay self-assessment tax, and file with DSC."
                }
            ],
            "compliance_checklist": [
                {"timeline": "September 30", "compliance": "Tax Audit Report (Form 3CA/3CD) Due Date"},
                {"timeline": "October 31", "compliance": "Corporate Income Tax Return (ITR-6) Due Date for audited entities"},
                {"timeline": "November 30", "compliance": "ITR-6 Due Date for companies subject to Transfer Pricing (Form 3CEB)"}
            ],
            "required_documents": [
                "Audited Financial Statements (P&L, Balance Sheet, Notes to Accounts)",
                "Form 26AS, AIS (Annual Information Statement), and TIS",
                "Challans for Advance Tax, Self-Assessment Tax, and TDS payments",
                "Depreciation Schedule under Income Tax Rules (Rule 5)"
            ]
        },
        "faqs": [
            {
                "question": "What is the corporate tax rate under the Section 115BAA concessional regime?",
                "answer": "Under Section 115BAA, domestic companies can opt for a flat 22% corporate tax rate (effective 25.17% including surcharge and cess), completely exempting the company from Minimum Alternate Tax (MAT)."
            }
        ]
    },
    {
        "guide_id": "dpdp-compliance-guide",
        "related_service_id": "data-privacy-dpdp-compliance",
        "title": "Digital Personal Data Protection Act (DPDP 2023): Enterprise Compliance Guide",
        "slug": "dpdp-compliance-guide",
        "category": "workforce-digital",
        "meta_description": "Comprehensive legal implementation guide for the Digital Personal Data Protection Act, 2023: Data Fiduciary duties, Consent Managers, Data Protection Officers, and penalty risk mitigation.",
        "read_time": "7 min read",
        "last_updated": "2026-10-31",
        "detailed_sections": {
            "overview": "The Digital Personal Data Protection Act, 2023 (DPDP Act) governs the processing of digital personal data within India. It establishes stringent obligations for corporate Data Fiduciaries and introduces penalties up to ₹250 Crores for data breaches.",
            "eligibility": [
                "Any business entity collecting, storing, processing, or transmitting digital personal data of Indian citizens.",
                "E-commerce platforms, SaaS providers, FinTech, EdTech, healthcare apps, and corporate employers."
            ],
            "step_by_step_procedure": [
                {
                    "step": 1,
                    "title": "Personal Data Inventory & Mapping",
                    "detail": "Catalog all customer, vendor, and employee data flows across digital databases, cloud servers, and CRM tools."
                },
                {
                    "step": 2,
                    "title": "Revamped Notice & Multilingual Consent Architecture",
                    "detail": "Implement clear, affirmative consent mechanisms offering data principals itemized opt-in choices in English and scheduled 22 Indian languages."
                },
                {
                    "step": 3,
                    "title": "Data Principal Rights Management System",
                    "detail": "Establish automated internal workflows to fulfill user requests for data access, correction, erasure, and grievance redressal."
                },
                {
                    "step": 4,
                    "title": "Appointment of Data Protection Officer (DPO)",
                    "detail": "Appoint an India-based Data Protection Officer and establish strict technical data security safeguards including encryption at rest."
                }
            ],
            "compliance_checklist": [
                {"timeline": "Immediate", "compliance": "Publish DPDP compliant Privacy Notice on all web & mobile properties"},
                {"timeline": "Within 72 Hours", "compliance": "Mandatory Data Breach Notification to Data Protection Board of India"},
                {"timeline": "Quarterly", "compliance": "Data audit and third-party processor agreement review"}
            ],
            "required_documents": [
                "Enterprise Data Flow Inventory Register",
                "Customer Privacy Policy & User Terms of Service",
                "Data Processing Agreements (DPA) with third-party vendors",
                "Standard Operating Procedure (SOP) for Incident Response and Breach Reporting"
            ]
        },
        "faqs": [
            {
                "question": "What is the maximum penalty for failure to prevent a data breach under DPDP Act?",
                "answer": "The Data Protection Board of India can impose monetary penalties up to ₹250 Crores for significant failure to take reasonable security safeguards to prevent personal data breaches."
            }
        ]
    }
]

def main():
    print("Compiling Craftegon Knowledge Hub...")
    output_payload = {
        "version": "2.0.0",
        "platform": "CraftEgon Corporate Services",
        "total_guides": len(GUIDES),
        "guides": GUIDES
    }

    os.makedirs('data', exist_ok=True)
    with open('data/craftegon-knowledge-hub.json', 'w', encoding='utf-8') as f:
        json.dump(output_payload, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated data/craftegon-knowledge-hub.json with {len(GUIDES)} authoritative guides!")

if __name__ == '__main__':
    main()
