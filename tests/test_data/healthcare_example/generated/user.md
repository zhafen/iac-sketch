#### AzNPDFSMPowerUserTeam

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 584


#### AzNPDResearchAnalyticsTeam

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 585


#### AzPRDFSMPowerUserTeam

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 586


#### AzPRDResearchAnalyticsTeam

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 587


#### accept_intake_form

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/intake_request.yaml

**input**

**node:**
- connected_component_group: 21

**output:**
- data_request [data_request]: The request, with details added by the intake form.

**task**


#### analyst_laptop

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 594


#### analyst_skills_assessment

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: analyst_skills_assessment
- target: can_approve_analyst_role
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### apply_security_groups_to_reports

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: apply_security_groups_to_pbi_reports
- target: apply_security_groups_to_reports
- link_type: parent

**link:**
- source: apply_security_groups_to_sharepoint_folders
- target: apply_security_groups_to_reports
- link_type: parent

**node:**
- connected_component_group: 8

**task**


#### assign_analyst

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/intake_request.yaml

**input**

**node:**
- connected_component_group: 21

**output:**
- data_request [data_request]: [{'modified_fields': {'has_data_steward_approval': None, 'has_completed_service_agreement': None}}]

**task**


#### azdo_work_item

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'id [int]': 'Number assigned to the work item by Azure Dev Ops.', 'assigned_to [str]': 'NM ID of the person the work is assigned to.', 'state [str]': 'State the work item is in.', 'tags [list[str]]': 'Tags associated with the work item.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'id': <Schema Field(name=id, type=DataType(int64))>, 'assigned_to': <Schema Field(name=assigned_to, type=DataType(str))>, 'state': <Schema Field(name=state, type=DataType(str))>, 'tags': <Schema Field(name=tags, type=None)>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'id [int]': 'Number assigned to the work item by Azure Dev Ops.', 'assigned_to [str]': 'NM ID of the person the work is assigned to.', 'state [str]': 'State the work item is in.', 'tags [list[str]]': 'Tags associated with the work item.'}

**node:**
- connected_component_group: 15


#### basic_report_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/testcases.yaml

**node:**
- connected_component_group: 596

**status**


#### brownbag

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 597

**url**


#### build_pbi_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/build_report.yaml

**link:**
- source: build_pbi_report
- target: retrieve_template_to_build_pbi_report_on
- link_type: depends_on

**link:**
- source: publish_pbi_report_to_stg
- target: build_pbi_report
- link_type: depends_on

**link:**
- source: get_feedback_on_pbi_report
- target: publish_pbi_report_to_stg
- link_type: depends_on

**links:** retrieve_template_to_build_pbi_report_on --> build_pbi_report
build_pbi_report --> publish_pbi_report_to_stg
publish_pbi_report_to_stg --> get_feedback_on_pbi_report

- link_type: depended_on_by

**node:**
- connected_component_group: 11

**task**


#### build_report_workflow

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/workflow.yaml

**link:**
- source: work_on_report
- target: get_feedback_on_report
- link_type: depends_on

**link:**
- source: finalize_report
- target: get_feedback_on_report
- link_type: depends_on

**link:**
- source: build_report_workflow
- target: can_build_reports
- link_type: satisfies

**link:**
- source: set_up_environment
- target: define_report
- link_type: depends_on

**link:**
- source: set_up_report
- target: set_up_environment
- link_type: depends_on

**link:**
- source: work_on_report
- target: set_up_report
- link_type: depends_on

**link:**
- source: get_feedback_on_report
- target: work_on_report
- link_type: depends_on

**links:** define_report --> set_up_environment
set_up_environment --> set_up_report
set_up_report --> work_on_report
work_on_report --> get_feedback_on_report
get_feedback_on_report --> work_on_report
get_feedback_on_report --> finalize_report

- link_type: depended_on_by

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### can_accept_and_process_request

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0

**task**


#### can_approve_analyst_role

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_approve_analyst_role
- target: can_hire_or_approve_analyst
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9

**satisfies**


#### can_approve_power_user

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_approve_power_user
- target: can_hire_or_approve_analyst
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9

**satisfies**


#### can_audit_data_access_and_usage

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: can_identify_patients_in_a_given_cohort_at_a_given_time
- target: can_audit_data_access_and_usage
- link_type: parent

**link:**
- source: can_inspect_data_access_history
- target: can_audit_data_access_and_usage
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_bill_power_users_for_charges

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/constraints.yaml

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.6


#### can_build_reports

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_call_llm

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 598

**requirement:**
- priority: 0.6


#### can_communicate_data_request_fulfillment_methodology

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 599

**requirement:**
- priority: 0.3


#### can_complete_requests_with_analysts

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: cloud_framework_is_usable
- target: can_complete_requests_with_analysts
- link_type: parent

**link:**
- source: can_support_and_manage_analysts
- target: can_complete_requests_with_analysts
- link_type: parent

**link:**
- source: can_complete_requests_with_analysts
- target: can_process_multiple_requests_in_parallel
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 1.0

**satisfies**


#### can_control_refresh_frequency

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** priority 0.6
- priority: 0.6


#### can_control_report_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_deliver_data_for_a_given_request

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: can_accept_and_process_request
- target: can_deliver_data_for_a_given_request
- link_type: parent

**link:**
- source: can_build_reports
- target: can_deliver_data_for_a_given_request
- link_type: parent

**link:**
- source: can_deliver_reports
- target: can_deliver_data_for_a_given_request
- link_type: parent

**link:**
- source: can_control_request_data_product_access
- target: can_deliver_data_for_a_given_request
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_deliver_nmedw_data_to_researchers

**child**

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: can_deliver_data_for_a_given_request
- target: can_deliver_nmedw_data_to_researchers
- link_type: parent

**link:**
- source: can_process_multiple_requests_in_parallel
- target: can_deliver_nmedw_data_to_researchers
- link_type: parent

**link:**
- source: can_audit_data_access_and_usage
- target: can_deliver_nmedw_data_to_researchers
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_deliver_reports

**child**

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: report_delivery_is_efficient
- target: can_deliver_reports
- link_type: parent

**link:**
- source: can_export_report_to_accessible_location
- target: can_deliver_reports
- link_type: parent

**link:**
- source: can_control_report_access
- target: can_deliver_reports
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0

**status**

**task**


#### can_estimate_report_expense

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/intake_request.yaml

**node:**
- connected_component_group: 601

**requirement:**
- priority: 0.5


#### can_export_report_to_accessible_location

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_get_approved_service_agreement

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/intake_request.yaml

**node:**
- connected_component_group: 602

**requirement:**
- priority: 0.5


#### can_get_data_steward_approval

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/intake_request.yaml

**node:**
- connected_component_group: 603

**requirement:**
- priority: 0.5


#### can_grant_access_to_analyst

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_grant_analyst_vm_access
- target: can_grant_access_to_analyst
- link_type: parent

**link:**
- source: can_grant_access_to_analyst
- target: can_onboard_analyst
- link_type: satisfies

**link:**
- source: can_grant_analyst_pa_account
- target: can_grant_access_to_analyst
- link_type: parent

**link:**
- source: can_grant_analyst_azdo_access
- target: can_grant_access_to_analyst
- link_type: parent

**link:**
- source: can_grant_analyst_databricks_access
- target: can_grant_access_to_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9

**satisfies**


#### can_grant_analyst_azdo_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_databricks_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_pa_account

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_vm_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_hire_or_approve_analyst

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_approve_analyst_role
- target: can_hire_or_approve_analyst
- link_type: parent

**link:**
- source: can_hire_ra_analyst
- target: can_hire_or_approve_analyst
- link_type: parent

**link:**
- source: can_approve_power_user
- target: can_hire_or_approve_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_hire_ra_analyst

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_hire_ra_analyst
- target: can_hire_or_approve_analyst
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.4

**satisfies**


#### can_identify_patients_in_a_given_cohort_at_a_given_time

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**parent**

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_inspect_data_access_history

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**parent**

**requirement:** research_analytics_infrastructure
- priority: 0.4


#### can_offboard_analyst

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_offboard_analyst
- target: support_and_manage_a_given_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**parent**

**requirement:**
- priority: 0.6


#### can_onboard_analyst

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_grant_access_to_analyst
- target: can_onboard_analyst
- link_type: parent

**link:**
- source: can_train_analyst
- target: can_onboard_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_pair_charges_to_power_users

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/constraints.yaml

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.6


#### can_process_multiple_requests_in_parallel

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_query_onprem_data

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**node:**
- connected_component_group: 604

**requirement:**
- priority: 1.0


#### can_recoup_costs_from_power_users

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/constraints.yaml

**link:**
- source: can_pair_charges_to_power_users
- target: can_recoup_costs_from_power_users
- link_type: parent

**link:**
- source: can_bill_power_users_for_charges
- target: can_recoup_costs_from_power_users
- link_type: parent

**link:**
- source: can_recoup_costs_from_power_users
- target: minimize_and_distribute_costs
- link_type: satisfies

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.6

**satisfies**


#### can_remove_analyst_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_remove_analyst_access
- target: offboard_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**parent**

**requirement:**
- priority: 0.6


#### can_support_analyst

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_support_analyst_in_primary_responsibilities
- target: can_support_analyst
- link_type: parent

**link:**
- source: can_support_analyst_in_logistical_responsibilities
- target: can_support_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_analyst_in_logistical_responsibilities

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_analyst_in_primary_responsibilities

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_and_manage_all_analyst_types

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_support_and_manage_an_analyst

**child**

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_offboard_analyst
- target: can_support_and_manage_an_analyst
- link_type: parent

**link:**
- source: can_remove_analyst_access
- target: can_support_and_manage_an_analyst
- link_type: parent

**link:**
- source: can_hire_or_approve_analyst
- target: can_support_and_manage_an_analyst
- link_type: parent

**link:**
- source: can_onboard_analyst
- target: can_support_and_manage_an_analyst
- link_type: parent

**link:**
- source: can_support_analyst
- target: can_support_and_manage_an_analyst
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_and_manage_analyst_teams

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_and_manage_analysts

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_support_and_manage_an_analyst
- target: can_support_and_manage_analysts
- link_type: parent

**link:**
- source: can_support_and_manage_analyst_teams
- target: can_support_and_manage_analysts
- link_type: parent

**link:**
- source: can_support_and_manage_all_analyst_types
- target: can_support_and_manage_analysts
- link_type: parent

**link:**
- source: can_support_and_manage_analysts
- target: can_complete_requests_with_analysts
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6

**satisfies**


#### can_train_analyst

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**link:**
- source: can_train_cloud_framework_users_on_usage
- target: can_train_analyst
- link_type: parent

**link:**
- source: can_train_analyst_in_logistical_responsibilities
- target: can_train_analyst
- link_type: parent

**link:**
- source: can_train_analyst
- target: can_onboard_analyst
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9

**satisfies**


#### can_train_analyst_in_logistical_responsibilities

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_train_cloud_framework_users

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/analyst_experience.yaml

**link:**
- source: can_train_cloud_framework_users
- target: cloud_framework_is_usable
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 1.0

**satisfies**


#### can_upskill_users

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/analyst_experience.yaml

**link:**
- source: can_upskill_users
- target: cloud_framework_is_usable
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6

**satisfies**


#### check_study_status

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 605

**task**


#### cloud_framework_documentation

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/resources.yaml

**link:**
- source: cloud_framework_wiki
- target: cloud_framework_documentation
- link_type: parent

**link:**
- source: cloud_framework_documentation
- target: cloud_framework_is_documented
- link_type: satisfies

**link:**
- source: ra_lib_docstrings
- target: cloud_framework_documentation
- link_type: parent

**link:**
- source: ra_lib_readme
- target: cloud_framework_documentation
- link_type: parent

**link:**
- source: ra_reports_readme
- target: cloud_framework_documentation
- link_type: parent

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### cloud_framework_helper_utilities

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/resources.yaml

**link:**
- source: cloud_framework_helper_utilities
- target: cloud_framework_is_user_friendly
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### cloud_framework_is_documented

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/analyst_experience.yaml

**link:**
- source: cloud_framework_is_documented
- target: cloud_framework_is_usable
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 1.0

**satisfies**


#### cloud_framework_is_usable

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/analyst_experience.yaml

**link:**
- source: cloud_framework_is_user_friendly
- target: cloud_framework_is_usable
- link_type: parent

**link:**
- source: cloud_framework_is_usable
- target: can_complete_requests_with_analysts
- link_type: satisfies

**link:**
- source: can_train_cloud_framework_users
- target: cloud_framework_is_usable
- link_type: parent

**link:**
- source: can_upskill_cloud_framework_users
- target: cloud_framework_is_usable
- link_type: parent

**link:**
- source: cloud_framework_is_documented
- target: cloud_framework_is_usable
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:**
- priority: 1.0

**satisfies**


#### cloud_framework_is_user_friendly

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/analyst_experience.yaml

**link:**
- source: cloud_framework_is_user_friendly
- target: cloud_framework_is_usable
- link_type: satisfies

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9

**satisfies**


#### cloud_framework_training_process

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/resources.yaml

**link:**
- source: cloud_framework_training_process
- target: can_train_cloud_framework_users
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### cloud_framework_user_experience_review_process

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/resources.yaml

**link:**
- source: cloud_framework_user_experience_review_process
- target: cloud_framework_is_user_friendly
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### cloud_reporting_framework

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**link:**
- source: cloud_reporting_framework
- target: can_deliver_nmedw_data_to_researchers
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**todo:** What name should we use for the overall infrastructure of research analytics? Currently the not-so-catchy name is Research Analytics Cloud Reporting Framework. RA Cloud? Research Analytics Azure Reporting (RAAR)?

- priority: 0.5


#### cohort

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': 'Unique ID for a cohort.', 'patients [list[str]]': 'IDs of patients in the cohort.', 'is_active [bool]': 'Cohorts become active after a specific time and de-activate later.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'patients': <Schema Field(name=patients, type=None)>, 'is_active': <Schema Field(name=is_active, type=DataType(bool))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': 'Unique ID for a cohort.', 'patients [list[str]]': 'IDs of patients in the cohort.', 'is_active [bool]': 'Cohorts become active after a specific time and de-activate later.'}

**node:**
- connected_component_group: 610


#### cohort_patient_change

**compdef:**
- component.table: cohort_patients_history
- multiplicity: 0..*
- unparsed_fields: {'report_id [report_id]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'change_type [categorical]': {'categories': ['inserted', 'deleted']}, 'change_datetime [timestamp]': 'When the change occurred.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=None)>, 'patient_id': <Schema Field(name=patient_id, type=DataType(str))>, 'patient_id_type': <Schema Field(name=patient_id_type, type=DataType(str))>, 'change_type': <Schema Field(name=change_type, type=DataType(category))>, 'change_datetime': <Schema Field(name=change_datetime, type=None)>}
- is_valid: True
- errors: 

**component:**
- table: cohort_patients_history

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [report_id]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'change_type [categorical]': {'categories': ['inserted', 'deleted']}, 'change_datetime [timestamp]': 'When the change occurred.'}

**node:**
- connected_component_group: 611

**representation_of**

**time_dependent:**
- scd_type: Type IV


#### cohort_patients

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'meta_updated_datetime [timestamp]': 'Time at which this entry was added.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'patient_id': <Schema Field(name=patient_id, type=DataType(str))>, 'patient_id_type': <Schema Field(name=patient_id_type, type=DataType(str))>, 'meta_updated_datetime': <Schema Field(name=meta_updated_datetime, type=None)>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'meta_updated_datetime [timestamp]': 'Time at which this entry was added.'}

**foreign_keys:**
- report_id: report.report_id
- patient_id: patient.patient_id
- patient_id_type: patient.patient_id_type

**node:**
- connected_component_group: 612

**representation_of**

**time_dependent:**
- scd_type: Type II


#### complete_data_steward_approval

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/intake_request.yaml

**link:**
- source: has_irb
- target: submit_for_data_steward_approval
- link_type: proceeded_by

**link:**
- source: has_irb
- target: return
- link_type: proceeded_by

**link:**
- source: submit_data_steward_approval
- target: wait_for_data_steward_approval
- link_type: proceeded_by

**link:**
- source: wait_for_data_steward_approval
- target: has_data_steward_approval
- link_type: proceeded_by

**link:**
- source: has_data_steward_approval
- target: return
- link_type: proceeded_by

**links:** has_irb --> submit_for_data_steward_approval
has_irb --> return
submit_data_steward_approval --> wait_for_data_steward_approval
wait_for_data_steward_approval --> has_data_steward_approval
has_data_steward_approval --> return

- link_type: proceeded_by

**node:**
- connected_component_group: 21


#### compliance_reports_suite

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/compliance.yaml

**link:**
- source: compliance_reports_suite
- target: can_audit_data_access_and_usage
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### corporate_compliance_team

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 616


#### cost_auditing_procedure

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: cost_auditing_procedure
- target: have_a_cost_auditing_procedure
- link_type: satisfies

**node:**
- connected_component_group: 13

**satisfies**

**status**


#### create_and_sync_security_groups

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**node:**
- connected_component_group: 8

**task**


#### create_pa_account

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 617

**task**

**url**


#### cross_institution_data_delivery

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 618


#### data_request

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'snow_universal_request_number [str]': 'SNow number for the overall task.', 'snow_data_steward_approval_task_number [str]': 'SNow number for data steward approval.', 'snow_service_agreement_task_number [str]': 'SNow number for the service agreement.', 'requester_id [str]': 'This will either be an NU ID via B2B or an NM ID.', 'irb_number [str]': 'Unless this is for de-identified data.', 'request_details [str]': 'As provided by the requester.', 'azdo_id [str]': None, 'assigned_to [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'snow_universal_request_number': <Schema Field(name=snow_universal_request_number, type=DataType(str))>, 'snow_data_steward_approval_task_number': <Schema Field(name=snow_data_steward_approval_task_number, type=DataType(str))>, 'snow_service_agreement_task_number': <Schema Field(name=snow_service_agreement_task_number, type=DataType(str))>, 'requester_id': <Schema Field(name=requester_id, type=DataType(str))>, 'irb_number': <Schema Field(name=irb_number, type=DataType(str))>, 'request_details': <Schema Field(name=request_details, type=DataType(str))>, 'azdo_id': <Schema Field(name=azdo_id, type=DataType(str))>, 'assigned_to': <Schema Field(name=assigned_to, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'snow_universal_request_number [str]': 'SNow number for the overall task.', 'snow_data_steward_approval_task_number [str]': 'SNow number for data steward approval.', 'snow_service_agreement_task_number [str]': 'SNow number for the service agreement.', 'requester_id [str]': 'This will either be an NU ID via B2B or an NM ID.', 'irb_number [str]': 'Unless this is for de-identified data.', 'request_details [str]': 'As provided by the requester.', 'azdo_id [str]': None, 'assigned_to [str]': None}

**foreign_keys:**
- requester_id: nm_compatible_identity.nm_id
- azdo_id: azdo_work_item.id
- assigned_to: nm_account.nm_id

**node:**
- connected_component_group: 619


#### data_request_work_item

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>}
- is_valid: True
- errors: 

**component**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**link:**
- source: data_request_work_item
- target: azdo_work_item
- link_type: parent

**node:**
- connected_component_group: 15

**parent**


#### databricks_workspace

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'url [str]': 'Unique URL for the workspace.', 'name [str]': 'Name for the wokspace.', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'url': <Schema Field(name=url, type=DataType(str))>, 'name': <Schema Field(name=name, type=DataType(str))>, 'deployment_environment': <Schema Field(name=deployment_environment, type=DataType(category))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**fields:**
- component: {'url [str]': 'Unique URL for the workspace.', 'name [str]': 'Name for the wokspace.', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}

**node:**
- connected_component_group: 620


#### databricks_workspace_volume

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 621

**path**


#### deliver_report_workflow

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/workflow.yaml

**link:**
- source: run_report
- target: deploy_report
- link_type: depends_on

**link:**
- source: share_report
- target: run_report
- link_type: depends_on

**link:**
- source: deliver_report_workflow
- target: can_deliver_reports
- link_type: satisfies

**links:** deploy_report --> run_report
run_report --> share_report

- link_type: depended_on_by

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### deploy_report

**code:**
- repo: ra_reports
- path: azure-pipelines.yaml

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**node:**
- connected_component_group: 8

**status**

**task**


#### discrepant_data_incident

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 626


#### download_report_from_fsmresfiles

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: fsmresfiles
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 628

**task**


#### download_report_from_pbi_workspace

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: pbi_workspace
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 629

**task**


#### download_report_from_teams

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: nunm_teams_sharepoint
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 630

**task**


#### edw_portal

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 631


#### entra_group

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'name [str]': 'The group name.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'name': <Schema Field(name=name, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'name [str]': 'The group name.'}

**node:**
- connected_component_group: 633

**question**

**question**

**question**

**question**

**question**

**question**

**question**

**question**


#### entra_id

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'id [str]': 'The actual ID.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'id': <Schema Field(name=id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'id [str]': 'The actual ID.'}

**node:**
- connected_component_group: 634


#### export_pbi_to_excel

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 635

**procedure**

**task**


#### export_report_data_products

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: export_report_data_products
- target: can_export_report_to_accessible_location
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### export_report_to_pbi_workspace

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: pbi_workspace
- link_type: flow

**node:**
- connected_component_group: 636

**task**


#### extracts_transfer_reports_to_fsmresfiles

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: fsmresfiles
- link_type: flow

**node:**
- connected_component_group: 637

**task**


#### extracts_transfer_reports_to_teams

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: nunm_teams_sharepoint
- link_type: flow

**node:**
- connected_component_group: 638

**task**


#### finalize_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/build_report.yaml

**link:**
- source: update_prd_pbi_with_prd_parameters
- target: publish_pbi_to_prd
- link_type: depends_on

**link:**
- source: validate_prd_report
- target: update_prd_pbi_with_prd_parameters
- link_type: depends_on

**link:**
- source: run_report_with_prd_workflow
- target: merge_pr
- link_type: depends_on

**link:**
- source: validate_prd_report
- target: run_report_with_prd_workflow
- link_type: depends_on

**links:** publish_pbi_to_prd --> update_prd_pbi_with_prd_parameters
update_prd_pbi_with_prd_parameters --> validate_prd_report
merge_pr --> run_report_with_prd_workflow
run_report_with_prd_workflow --> validate_prd_report

- link_type: depended_on_by

**node:**
- connected_component_group: 12

**task**


#### forgotten_ticket_incident

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 641


#### fsm_analyst_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None, 'nu_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>, 'nu_id': <Schema Field(name=nu_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None, 'nu_id [str]': None}

**foreign_keys:**
- nm_id: nm_role.nm_id
- nu_id: nu_role.nu_id

**node:**
- connected_component_group: 642

**primary_key**


#### fsm_finance_nm_security_group

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**name**

**node:**
- connected_component_group: 643

**url**


#### get_feedback_on_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/build_report.yaml

**link:**
- source: revise_pr
- target: get_feedback_from_second_reviewer
- link_type: depends_on

**link:**
- source: get_feedback_from_second_reviewer
- target: revise_pr
- link_type: depends_on

**link:**
- source: update_pbi_data_connections
- target: run_report_with_stg_workflow
- link_type: depends_on

**link:**
- source: publish_pbi_to_stg
- target: update_pbi_data_connections
- link_type: depends_on

**link:**
- source: submit_pr
- target: publish_pbi_to_stg
- link_type: depends_on

**link:**
- source: get_feedback_from_first_reviewer
- target: submit_pr
- link_type: depends_on

**link:**
- source: revise_pr
- target: get_feedback_from_first_reviewer
- link_type: depends_on

**link:**
- source: get_feedback_from_first_reviewer
- target: revise_pr
- link_type: depends_on

**link:**
- source: get_feedback_from_second_reviewer
- target: get_feedback_from_first_reviewer
- link_type: depends_on

**links:** run_report_with_stg_workflow --> update_pbi_data_connections
update_pbi_data_connections --> publish_pbi_to_stg
publish_pbi_to_stg --> submit_pr
submit_pr --> get_feedback_from_first_reviewer
get_feedback_from_first_reviewer --> revise_pr
revise_pr --> get_feedback_from_first_reviewer
get_feedback_from_first_reviewer --> get_feedback_from_second_reviewer
get_feedback_from_second_reviewer --> revise_pr
revise_pr --> get_feedback_from_second_reviewer

- link_type: depended_on_by

**node:**
- connected_component_group: 12

**task**


#### grant_analyst_access

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: grant_analyst_databricks_access
- target: grant_analyst_access
- link_type: parent

**link:**
- source: grant_analyst_vm_access
- target: grant_analyst_access
- link_type: parent

**link:**
- source: grant_analyst_access
- target: can_grant_access_to_analyst
- link_type: satisfies

**link:**
- source: grant_analyst_pa_account
- target: grant_analyst_access
- link_type: parent

**link:**
- source: grant_analyst_azdo_access
- target: grant_analyst_access
- link_type: parent

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### grant_analyst_azdo_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: grant_analyst_azdo_access
- target: can_grant_analyst_azdo_access
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### grant_analyst_databricks_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: grant_analyst_databricks_access
- target: can_grant_analyst_databricks_access
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### grant_analyst_pa_account

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: grant_analyst_pa_account
- target: can_grant_analyst_pa_account
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### grant_analyst_vm_access

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: grant_analyst_vm_access
- target: can_grant_analyst_vm_access
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### have_a_cost_auditing_procedure

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/constraints.yaml

**link:**
- source: have_a_cost_auditing_procedure
- target: minimize_and_distribute_costs
- link_type: satisfies

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.9

**satisfies**


#### intake_request_workflow

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/workflow.yaml

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/intake_request.yaml

**link:**
- source: complete_data_steward_approval
- target: assign_analyst
- link_type: depends_on

**link:**
- source: prepare_request_for_work
- target: complete_service_agreement
- link_type: depends_on

**link:**
- source: prepare_request_for_work
- target: complete_data_steward_approval
- link_type: depends_on

**link:**
- source: intake_request_workflow
- target: can_accept_and_process_request
- link_type: satisfies

**link:**
- source: assign_analyst
- target: accept_intake_form
- link_type: depends_on

**link:**
- source: complete_service_agreement
- target: assign_analyst
- link_type: depends_on

**links:** accept_intake_form --> assign_analyst
assign_analyst --> complete_service_agreement
assign_analyst --> complete_data_steward_approval
complete_service_agreement --> prepare_request_for_work
complete_data_steward_approval --> prepare_request_for_work

- link_type: depended_on_by

**node:**
- connected_component_group: 8

**satisfies**

**satisfies**

**status**

**status**


#### irb_pbi_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**link:**
- source: irb_pbi_report
- target: pbi_report
- link_type: parent

**node:**
- connected_component_group: 22

**parent**

**path**


#### irb_report_code_product

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**link:**
- source: irb_report_code_product
- target: report_code_product
- link_type: parent

**node:**
- connected_component_group: 23

**parent**

**path**


#### logistical_training

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: logistical_training
- target: can_train_analyst_in_logistical_responsibilities
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### management_framework

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: management_framework
- target: can_support_and_manage_analysts
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### minimize_and_distribute_costs

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/constraints.yaml

**link:**
- source: have_a_cost_auditing_procedure
- target: minimize_and_distribute_costs
- link_type: parent

**link:**
- source: can_recoup_costs_from_power_users
- target: minimize_and_distribute_costs
- link_type: parent

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.9


#### nm_compatible_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': 'Unique identifier.', 'identity_type [categorical]': {'description': 'Type of identity.', 'categories': ['employee', 'person_of_interest', 'b2b']}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>, 'identity_type': <Schema Field(name=identity_type, type=DataType(category))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': 'Unique identifier.', 'identity_type [categorical]': {'description': 'Type of identity.', 'categories': ['employee', 'person_of_interest', 'b2b']}}

**node:**
- connected_component_group: 652


#### nm_data_portal

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 653


#### nm_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None, 'pa_id [str]': 'If the user has a privileged access account.', 'job_code [str]': 'Unique identifier for their job.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>, 'pa_id': <Schema Field(name=pa_id, type=DataType(str))>, 'job_code': <Schema Field(name=job_code, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None, 'pa_id [str]': 'If the user has a privileged access account.', 'job_code [str]': 'Unique identifier for their job.'}

**node:**
- connected_component_group: 654


#### no_irb_test

**data_request:**
- requester_id: net002@ads.northwestern.edu

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/testcases.yaml

**node:**
- connected_component_group: 655

**status**


#### noirb_pbi_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**link:**
- source: noirb_pbi_report
- target: pbi_report
- link_type: parent

**node:**
- connected_component_group: 22

**parent**

**path**


#### noirb_report_code_product

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**link:**
- source: noirb_report_code_product
- target: report_code_product
- link_type: parent

**node:**
- connected_component_group: 23

**parent**

**path**


#### northwestern_university_fsm_it

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 658


#### nu_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'net_id [str]': 'Unique identifier for NU.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'net_id': <Schema Field(name=net_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'net_id [str]': 'Unique identifier for NU.'}

**node:**
- connected_component_group: 659


#### patient

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'patient_id [str]': 'The unique identifier for the patient, in combination with patient_id_type.\n', 'patient_id_type [categorical]': {'categories': ['nm_bi.ir_id', 'clarity.pat_id', 'mock.mock_id']}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'patient_id': <Schema Field(name=patient_id, type=DataType(str))>, 'patient_id_type': <Schema Field(name=patient_id_type, type=DataType(category))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'patient_id [str]': 'The unique identifier for the patient, in combination with patient_id_type.\n', 'patient_id_type [categorical]': {'categories': ['nm_bi.ir_id', 'clarity.pat_id', 'mock.mock_id']}}

**node:**
- connected_component_group: 663

**primary_key**

**primary_key**

**time_dependent**


#### pbi_app_homepage

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**node:**
- connected_component_group: 664


#### pbi_report

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': None, 'description [str]': 'This description will show up in the portal.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'description': <Schema Field(name=description, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': None, 'description [str]': 'This description will show up in the portal.'}

**node:**
- connected_component_group: 22


#### pbi_workspace_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'user [person]': 'The user for the role.', 'workspace [workspace]': 'The PBI workspace in question.', 'role [categorical]': 'The PBI role.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'user': <Schema Field(name=user, type=None)>, 'workspace': <Schema Field(name=workspace, type=None)>, 'role': <Schema Field(name=role, type=DataType(category))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'user [person]': 'The user for the role.', 'workspace [workspace]': 'The PBI workspace in question.', 'role [categorical]': 'The PBI role.'}

**node:**
- connected_component_group: 665


#### power_user_approval_process

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: power_user_approval_process
- target: can_approve_power_user
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### power_user_jira_project

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 666


#### power_user_office_hours

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 667


#### power_user_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'entra_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'entra_id': <Schema Field(name=entra_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'entra_id [str]': None}

**foreign_keys:**
- nm_id: fsm_analyst_role.nm_id

**node:**
- connected_component_group: 668


#### power_user_sharepoint

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 669

**url**


#### power_users_azdo_project

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 670


#### power_users_management_framework

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: power_users_management_framework
- target: can_support_and_manage_all_analyst_types
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### pu_reports

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 672


#### ra_lib

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 675


#### ra_lib_repo

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**git_repo:**
- url: https://NMHC@dev.azure.com/NMHC/FSM%20Research%20Analytics/_git/ra_lib

**node:**
- connected_component_group: 676


#### ra_reports

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 677


#### ra_reports_branch

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'azdo_id [str]': 'Work item associated with this branch.', 'branch [git_branch]': 'The git branch component itself.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'azdo_id': <Schema Field(name=azdo_id, type=DataType(str))>, 'branch': <Schema Field(name=branch, type=None)>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'azdo_id [str]': 'Work item associated with this branch.', 'branch [git_branch]': 'The git branch component itself.'}

**foreign_keys:**
- azdo_id: data_request_work_item.id

**node:**
- connected_component_group: 678


#### ra_reports_repo

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**git_repo:**
- url: https://NMHC@dev.azure.com/NMHC/FSM%20Research%20Analytics/_git/ra_reports

**node:**
- connected_component_group: 679


#### ra_team_member_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'entra_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'entra_id': <Schema Field(name=entra_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'entra_id [str]': None}

**foreign_keys:**
- nm_id: fsm_analyst_role.nm_id

**node:**
- connected_component_group: 680


#### recruitment_compliance_constraints

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 681

**url**


#### report

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': 'ID for the report, {irb_number}.{irb_rank:.02d} (e.g. STU001234.01)', 'irb_number [str]': 'IRB number for the study associated with the report.', 'irb_rank [int]': 'IRB rank is defined as the number of reports associated with a study at the time of request intake, counting the report itself. As such, IRB rank starts at 1 and increases in steps of 1. When doing a partition over irb_number ordered by created_date ascending this is the row number.\n', 'pbi_workspace [str]': 'Which Power BI workspace the report lives in.', 'inserted_datetime [timestamp]': 'Date when the report was created, i.e. the product_id was created and we started tracking report status.\n', 'data_steward_approval [bool]': 'Whether or not the data has been approved for release.', 'description [str]': 'Description for the report.'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'irb_number': <Schema Field(name=irb_number, type=DataType(str))>, 'irb_rank': <Schema Field(name=irb_rank, type=DataType(int64))>, 'pbi_workspace': <Schema Field(name=pbi_workspace, type=DataType(str))>, 'inserted_datetime': <Schema Field(name=inserted_datetime, type=None)>, 'data_steward_approval': <Schema Field(name=data_steward_approval, type=DataType(bool))>, 'description': <Schema Field(name=description, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': 'ID for the report, {irb_number}.{irb_rank:.02d} (e.g. STU001234.01)', 'irb_number [str]': 'IRB number for the study associated with the report.', 'irb_rank [int]': 'IRB rank is defined as the number of reports associated with a study at the time of request intake, counting the report itself. As such, IRB rank starts at 1 and increases in steps of 1. When doing a partition over irb_number ordered by created_date ascending this is the row number.\n', 'pbi_workspace [str]': 'Which Power BI workspace the report lives in.', 'inserted_datetime [timestamp]': 'Date when the report was created, i.e. the product_id was created and we started tracking report status.\n', 'data_steward_approval [bool]': 'Whether or not the data has been approved for release.', 'description [str]': 'Description for the report.'}

**node:**
- connected_component_group: 683

**primary_key**


#### report_code_product

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': None, 'filename [str]': None, 'notebook_type [categorical]': {'categories': ['etl', 'cohort', 'report']}, 'git_branch [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'filename': <Schema Field(name=filename, type=DataType(str))>, 'notebook_type': <Schema Field(name=notebook_type, type=DataType(category))>, 'git_branch': <Schema Field(name=git_branch, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': None, 'filename [str]': None, 'notebook_type [categorical]': {'categories': ['etl', 'cohort', 'report']}, 'git_branch [str]': None}

**node:**
- connected_component_group: 23


#### report_configuration

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'azdo_id [str]': 'There is one and only one Azure DevOps work item per report configuration.\n', 'report_id [str]': 'ID of the report the Azure DevOps work item is associated with. For reports with IRBs this is based on the IRB number and the number of other reports for the same study. For reports without an IRB this is based on the Azure DevOps ID of the original work item.\n', 'irb_number [str]': 'Study number if provided, e.g. STU00000000.', 'assigned_to [str]': 'Individual the work item is assigned to.', 'domain [str]': 'Power BI Domain for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace [str]': 'Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace_folder [str]': 'Folder in the Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'report_dir_pattern [str]': 'Unix filename pattern specifying the directory inside the ra_reports repo that contains the report code.\n', 'azdo_title [str]': 'Title of the work item.', 'state [str]': "State of the work item, e.g. 'In Progress' or 'Closed'.", 'tags [str]': 'Tags associated with the work item.', 'predecessor_azdo_id [str]': "Azure DevOps work item ID of a predecessor linked in the work item. If a work item has a predecessor that is also a report work item (has the 'Report' tag), then the work item is an update to the original report.\n", 'is_active [str]': "If True, then this report is actively refreshed, using the metadata specified by this row. Each work item associated with a report can have an 'is_active' field in the yaml metadata, but only the most recent active work item (largest azdo_id with is_active == True) will be marked as active in this config table. When not specified, is_active defaults to True for work items with state == 'Closed'.\n", 'refresh_schedule [str]': 'Specification of how often the report should be executed.', 'irb_is_active [str]': 'For reports with an IRB, whether or not that IRB is active.', 'is_visible [str]': 'Whether or not any generated data should be visible to the end users.\n', 'description [str]': 'Description field for the work item. Some values have been extracted from her , e.g. irb_number.\n', 'is_valid [str]': 'If False, then some aspect of the work item is incorrectly defined, and this work item will not be used in production. Check the error_log field for details on the issue.\n', 'error_log [str]': 'Any recorded details on why a given work item may be invalid for specifying report metadata\n'}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'azdo_id': <Schema Field(name=azdo_id, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'irb_number': <Schema Field(name=irb_number, type=DataType(str))>, 'assigned_to': <Schema Field(name=assigned_to, type=DataType(str))>, 'domain': <Schema Field(name=domain, type=DataType(str))>, 'workspace': <Schema Field(name=workspace, type=DataType(str))>, 'workspace_folder': <Schema Field(name=workspace_folder, type=DataType(str))>, 'report_dir_pattern': <Schema Field(name=report_dir_pattern, type=DataType(str))>, 'azdo_title': <Schema Field(name=azdo_title, type=DataType(str))>, 'state': <Schema Field(name=state, type=DataType(str))>, 'tags': <Schema Field(name=tags, type=DataType(str))>, 'predecessor_azdo_id': <Schema Field(name=predecessor_azdo_id, type=DataType(str))>, 'is_active': <Schema Field(name=is_active, type=DataType(str))>, 'refresh_schedule': <Schema Field(name=refresh_schedule, type=DataType(str))>, 'irb_is_active': <Schema Field(name=irb_is_active, type=DataType(str))>, 'is_visible': <Schema Field(name=is_visible, type=DataType(str))>, 'description': <Schema Field(name=description, type=DataType(str))>, 'is_valid': <Schema Field(name=is_valid, type=DataType(str))>, 'error_log': <Schema Field(name=error_log, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'azdo_id [str]': 'There is one and only one Azure DevOps work item per report configuration.\n', 'report_id [str]': 'ID of the report the Azure DevOps work item is associated with. For reports with IRBs this is based on the IRB number and the number of other reports for the same study. For reports without an IRB this is based on the Azure DevOps ID of the original work item.\n', 'irb_number [str]': 'Study number if provided, e.g. STU00000000.', 'assigned_to [str]': 'Individual the work item is assigned to.', 'domain [str]': 'Power BI Domain for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace [str]': 'Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace_folder [str]': 'Folder in the Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'report_dir_pattern [str]': 'Unix filename pattern specifying the directory inside the ra_reports repo that contains the report code.\n', 'azdo_title [str]': 'Title of the work item.', 'state [str]': "State of the work item, e.g. 'In Progress' or 'Closed'.", 'tags [str]': 'Tags associated with the work item.', 'predecessor_azdo_id [str]': "Azure DevOps work item ID of a predecessor linked in the work item. If a work item has a predecessor that is also a report work item (has the 'Report' tag), then the work item is an update to the original report.\n", 'is_active [str]': "If True, then this report is actively refreshed, using the metadata specified by this row. Each work item associated with a report can have an 'is_active' field in the yaml metadata, but only the most recent active work item (largest azdo_id with is_active == True) will be marked as active in this config table. When not specified, is_active defaults to True for work items with state == 'Closed'.\n", 'refresh_schedule [str]': 'Specification of how often the report should be executed.', 'irb_is_active [str]': 'For reports with an IRB, whether or not that IRB is active.', 'is_visible [str]': 'Whether or not any generated data should be visible to the end users.\n', 'description [str]': 'Description field for the work item. Some values have been extracted from her , e.g. irb_number.\n', 'is_valid [str]': 'If False, then some aspect of the work item is incorrectly defined, and this work item will not be used in production. Check the error_log field for details on the issue.\n', 'error_log [str]': 'Any recorded details on why a given work item may be invalid for specifying report metadata\n'}

**foreign_keys:**
- report_id: report.report_id
- azdo_id: data_request_work_item.id

**name**

**node:**
- connected_component_group: 684

**primary_key**


#### report_delivery_is_efficient

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/requirements/functional.yaml

**link:**
- source: can_control_refresh_frequency
- target: report_delivery_is_efficient
- link_type: parent

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 0.5


#### report_table

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'label': <Schema Field(name=label, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}

**node:**
- connected_component_group: 685

**path**


#### request_workflow

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/workflow.yaml

**link:**
- source: build_report
- target: intake_request
- link_type: depends_on

**link:**
- source: deliver_report
- target: build_report
- link_type: depends_on

**link:**
- source: request_workflow
- target: can_deliver_data_for_a_given_request
- link_type: satisfies

**links:** intake_request --> build_report
build_report --> deliver_report

- link_type: depended_on_by

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### requester

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 687


#### research_analytics_azdo_project

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**node:**
- connected_component_group: 689


#### research_analytics_infrastructure

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**infrastructure**

**node:**
- connected_component_group: 690


#### research_analytics_pbi_workspace

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'workspace_name [str]': 'E.g. "Research Core".', 'workspace_domain [str]': 'E.g. "Research IRB".', 'workspace_folders [list[str]]': 'E.g. "NUCATS, Study Tracker, FSMIT".', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'workspace_name': <Schema Field(name=workspace_name, type=DataType(str))>, 'workspace_domain': <Schema Field(name=workspace_domain, type=DataType(str))>, 'workspace_folders': <Schema Field(name=workspace_folders, type=None)>, 'deployment_environment': <Schema Field(name=deployment_environment, type=DataType(category))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/infrastructure.yaml

**fields:**
- component: {'workspace_name [str]': 'E.g. "Research Core".', 'workspace_domain [str]': 'E.g. "Research IRB".', 'workspace_folders [list[str]]': 'E.g. "NUCATS, Study Tracker, FSMIT".', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}

**node:**
- connected_component_group: 691


#### rhlcc_group

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'entra_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'entra_id': <Schema Field(name=entra_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'entra_id [str]': None}

**node:**
- connected_component_group: 692


#### run_report

**code:**
- repo: ra_reports
- path: workflow/main.yaml

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**node:**
- connected_component_group: 8

**status**

**task**


#### set_report_access

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**link:**
- source: create_and_sync_security_groups
- target: set_report_access
- link_type: parent

**link:**
- source: apply_security_groups_to_reports
- target: set_report_access
- link_type: parent

**link:**
- source: set_report_access
- target: can_control_report_access
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**

**task**


#### share_report

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: share_pbi_dashboard
- target: share_report
- link_type: parent

**link:**
- source: export_report_data_products
- target: share_report
- link_type: parent

**node:**
- connected_component_group: 8

**task**


#### sharepoint_report_data_export

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'report_id': <Schema Field(name=report_id, type=DataType(str))>, 'label': <Schema Field(name=label, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}

**node:**
- connected_component_group: 695

**path**


#### support_team_member

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nu_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nu_id': <Schema Field(name=nu_id, type=DataType(str))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/access.yaml

**fields:**
- component: {'nu_id [str]': None}

**foreign_keys:**
- nu_id: nu_role.nu_id

**node:**
- connected_component_group: 697


#### time_dependent

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'scd_type [str]': {'description': 'Slowly changing dimension type.', 'categories': ['Type 0', 'Type 1', 'Type 2', 'Type 3', 'Type 4']}}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'scd_type': <Schema Field(name=scd_type, type=DataType(category))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'scd_type [str]': {'description': 'Slowly changing dimension type.', 'categories': ['Type 0', 'Type 1', 'Type 2', 'Type 3', 'Type 4']}}

**node:**
- connected_component_group: 700


#### training_plan_for_stem_opt_students

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 701


#### training_process

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/manage.yaml

**link:**
- source: logistical_training
- target: training_process
- link_type: parent

**link:**
- source: training_process
- target: can_train_analyst
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### turn_on_pbi_refresh

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**node:**
- connected_component_group: 703

**task**


#### updated_report_new_analyst_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/testcases.yaml

**node:**
- connected_component_group: 704

**status**


#### updated_report_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/testcases.yaml

**node:**
- connected_component_group: 705

**status**


#### variable_naming_conventions

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/unsorted.yaml

**node:**
- connected_component_group: 707


#### work_on_report

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/build_report.yaml

**link:**
- source: build_report
- target: build_cohort
- link_type: depends_on

**link:**
- source: build_pbi_report
- target: build_report
- link_type: depends_on

**links:** build_cohort --> build_report
build_report --> build_pbi_report

- link_type: depended_on_by

**node:**
- connected_component_group: 12

**task**


#### worklog

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'worklog_id [int]': None, 'azdo_id [int]': None, 'user_id [str]': None, 'timestamp [timestamp]': None, 'duration [float]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'worklog_id': <Schema Field(name=worklog_id, type=DataType(int64))>, 'azdo_id': <Schema Field(name=azdo_id, type=DataType(int64))>, 'user_id': <Schema Field(name=user_id, type=DataType(str))>, 'timestamp': <Schema Field(name=timestamp, type=None)>, 'duration': <Schema Field(name=duration, type=DataType(float64))>}
- is_valid: True
- errors: 

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/data.yaml

**fields:**
- component: {'worklog_id [int]': None, 'azdo_id [int]': None, 'user_id [str]': None, 'timestamp [timestamp]': None, 'duration [float]': None}

**foreign_keys:**
- azdo_id: azdo_work_item.id
- user_id: nm_account.nm_id

**node:**
- connected_component_group: 708


#### write_report_to_catalog

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: databricks_prd_catalog
- link_type: flow

**node:**
- connected_component_group: 709

**task**


#### write_report_to_sharepoint

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: nunm_teams_sharepoint
- link_type: flow

**node:**
- connected_component_group: 710

**task**


#### write_report_to_volume

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/**/*.yaml
- filename: /Users/zhafen/repos/iaca/tests/test_data/healthcare_example/manifest/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: databricks_prd_volume
- link_type: flow

**node:**
- connected_component_group: 711

**task**


