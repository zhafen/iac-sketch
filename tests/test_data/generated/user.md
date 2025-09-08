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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 587


#### accept_intake_form

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/intake_request.yaml

**input**

**node:**
- connected_component_group: 23

**output:**
- data_request [data_request]: The request, with details added by the intake form.

**task**


#### analyst_laptop

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 594


#### analyst_skills_assessment

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/intake_request.yaml

**input**

**node:**
- connected_component_group: 23

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'id [int]': 'Number assigned to the work item by Azure Dev Ops.', 'assigned_to [str]': 'NM ID of the person the work is assigned to.', 'state [str]': 'State the work item is in.', 'tags [list[str]]': 'Tags associated with the work item.'}

**node:**
- connected_component_group: 16


#### basic_report_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/testcases.yaml

**node:**
- connected_component_group: 596

**status**


#### build_pbi_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/build_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/workflow.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0

**task**


#### can_approve_analyst_role

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/constraints.yaml

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.6


#### can_build_reports

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_call_llm

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 597

**requirement:**
- priority: 0.6


#### can_communicate_data_request_fulfillment_methodology

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 598

**requirement:**
- priority: 0.3


#### can_complete_requests_with_analysts

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** priority 0.6
- priority: 0.6


#### can_control_report_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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


#### can_export_report_to_accessible_location

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_grant_access_to_analyst

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_databricks_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_pa_account

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_grant_analyst_vm_access

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**parent**

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_inspect_data_access_history

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**parent**

**requirement:** research_analytics_infrastructure
- priority: 0.4


#### can_offboard_analyst

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/constraints.yaml

**node:**
- connected_component_group: 13

**requirement:** research_analytics_infrastructure
- priority: 0.6


#### can_process_multiple_requests_in_parallel

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 8

**requirement:** research_analytics_infrastructure
- priority: 1.0


#### can_query_onprem_data

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

**node:**
- connected_component_group: 19

**requirement:**
- priority: 1.0


#### can_recoup_costs_from_power_users

**child**

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/constraints.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_analyst_in_primary_responsibilities

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.6


#### can_support_and_manage_all_analyst_types

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/organizational.yaml

**node:**
- connected_component_group: 8

**requirement:**
- priority: 0.9


#### can_train_cloud_framework_users

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/analyst_experience.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/analyst_experience.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 600

**task**


#### cloud_framework_documentation

**child**

**child**

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/resources.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/resources.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/analyst_experience.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/analyst_experience.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/analyst_experience.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/resources.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/resources.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': 'Unique ID for a cohort.', 'patients [list[str]]': 'IDs of patients in the cohort.', 'is_active [bool]': 'Cohorts become active after a specific time and de-activate later.'}

**node:**
- connected_component_group: 14


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [report_id]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'change_type [categorical]': {'categories': ['inserted', 'deleted']}, 'change_datetime [timestamp]': 'When the change occurred.'}

**link:**
- source: cohort_patient_change
- target: cohort
- link_type: transformation_of

**node:**
- connected_component_group: 14

**time_dependent:**
- scd_type: Type IV

**transformation_of**


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': None, 'patient_id [str]': None, 'patient_id_type [str]': None, 'meta_updated_datetime [timestamp]': 'Time at which this entry was added.'}

**foreign_keys:**
- report_id: report.report_id
- patient_id: patient.patient_id
- patient_id_type: patient.patient_id_type

**link:**
- source: cohort_patients
- target: cohort
- link_type: transformation_of

**node:**
- connected_component_group: 14

**time_dependent:**
- scd_type: Type II

**transformation_of**


#### complete_data_steward_approval

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/intake_request.yaml

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
- connected_component_group: 23


#### compliance_reports_suite

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/compliance.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 608


#### cost_auditing_procedure

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**node:**
- connected_component_group: 8

**task**


#### create_pa_account

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 609

**task**

**url**


#### cross_institution_data_delivery

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 610


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'snow_universal_request_number [str]': 'SNow number for the overall task.', 'snow_data_steward_approval_task_number [str]': 'SNow number for data steward approval.', 'snow_service_agreement_task_number [str]': 'SNow number for the service agreement.', 'requester_id [str]': 'This will either be an NU ID via B2B or an NM ID.', 'irb_number [str]': 'Unless this is for de-identified data.', 'request_details [str]': 'As provided by the requester.', 'azdo_id [str]': None, 'assigned_to [str]': None}

**foreign_keys:**
- requester_id: nm_compatible_identity.nm_id
- azdo_id: azdo_work_item.id
- assigned_to: nm_account.nm_id

**node:**
- connected_component_group: 611


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**link:**
- source: data_request_work_item
- target: azdo_work_item
- link_type: parent

**node:**
- connected_component_group: 16

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**fields:**
- component: {'url [str]': 'Unique URL for the workspace.', 'name [str]': 'Name for the wokspace.', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}

**node:**
- connected_component_group: 612


#### databricks_workspace_volume

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 613

**path**


#### deliver_report_workflow

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/workflow.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**node:**
- connected_component_group: 8

**status**

**task**


#### discrepant_data_incident

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 618


#### download_report_from_fsmresfiles

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: fsmresfiles
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 620

**task**


#### download_report_from_pbi_workspace

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: pbi_workspace
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 621

**task**


#### download_report_from_teams

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: nunm_teams_sharepoint
- target: requester_computer
- link_type: flow

**node:**
- connected_component_group: 622

**task**


#### edw_portal

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 623


#### example_manifest/__init__

**Module:**
- body: []
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/__init__.py

**node:**
- connected_component_group: 625


#### example_manifest/assistant

**Module:**
- body: ['example_manifest/assistant.0', 'example_manifest/assistant.1', 'example_manifest/assistant.2', 'example_manifest/assistant.3', 'example_manifest/assistant.4', 'example_manifest/assistant.5', 'example_manifest/assistant.6', 'example_manifest/assistant.7', 'example_manifest/assistant.8', 'example_manifest/assistant.9', 'example_manifest/assistant.10', 'example_manifest/assistant.11', 'example_manifest/assistant.12', 'example_manifest/assistant.13', 'example_manifest/assistant.14', 'example_manifest/assistant.15', 'example_manifest/assistant.16', 'example_manifest/assistant.17', 'example_manifest/assistant.18', 'example_manifest/assistant.ResearchAssistant']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 626


#### example_manifest/assistant.0

**Import:**
- names: [{'name': 'base64', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 627


#### example_manifest/assistant.1

**Import:**
- names: [{'name': 'glob', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 628


#### example_manifest/assistant.10

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 629


#### example_manifest/assistant.11

**ImportFrom:**
- module: pyspark.sql.dataframe
- names: [{'name': 'DataFrame', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 630


#### example_manifest/assistant.12

**ImportFrom:**
- module: pyspark.sql.functions
- names: [{'name': 'lit', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 631


#### example_manifest/assistant.13

**Import:**
- names: [{'name': 'sqlalchemy', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 632


#### example_manifest/assistant.14

**ImportFrom:**
- names: [{'name': 'environment', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 633


#### example_manifest/assistant.15

**ImportFrom:**
- names: [{'name': 'utils', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 634


#### example_manifest/assistant.16

**ImportFrom:**
- names: [{'name': 'cohort', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 635


#### example_manifest/assistant.17

**ImportFrom:**
- names: [{'name': 'query', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 636


#### example_manifest/assistant.18

**ImportFrom:**
- names: [{'name': 'azdo', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 637


#### example_manifest/assistant.2

**Import:**
- names: [{'name': 'os', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 638


#### example_manifest/assistant.3

**Import:**
- names: [{'name': 'shutil', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 639


#### example_manifest/assistant.4

**Import:**
- names: [{'name': 'time', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 640


#### example_manifest/assistant.5

**ImportFrom:**
- module: databricks.sdk
- names: [{'name': 'WorkspaceClient', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 641


#### example_manifest/assistant.6

**ImportFrom:**
- module: databricks.sdk.service
- names: [{'name': 'workspace', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 642


#### example_manifest/assistant.7

**Import:**
- names: [{'name': 'networkx', 'asname': 'nx'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 643


#### example_manifest/assistant.8

**Import:**
- names: [{'name': 'numpy', 'asname': 'np'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 644


#### example_manifest/assistant.9

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 645


#### example_manifest/assistant.ResearchAssistant

**ClassDef:**
- name: ResearchAssistant
- bases: []
- keywords: []
- body: ['example_manifest/assistant.ResearchAssistant', 'example_manifest/assistant.ResearchAssistant.__init__', 'example_manifest/assistant.ResearchAssistant.get_report_config', 'example_manifest/assistant.ResearchAssistant.generate_reports_config', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base', 'example_manifest/assistant.ResearchAssistant.add_report_ids', 'example_manifest/assistant.ResearchAssistant.add_report_locations', 'example_manifest/assistant.ResearchAssistant.get_valid_report_locations', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config', 'example_manifest/assistant.ResearchAssistant.write_reports_config', 'example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh', 'example_manifest/assistant.ResearchAssistant.draft_report_structure', 'example_manifest/assistant.ResearchAssistant.build_report_structure', 'example_manifest/assistant.ResearchAssistant.get', 'example_manifest/assistant.ResearchAssistant.set', 'example_manifest/assistant.ResearchAssistant.save_report_table', 'example_manifest/assistant.ResearchAssistant.load_cohort', 'example_manifest/assistant.ResearchAssistant.save_cohort', 'example_manifest/assistant.ResearchAssistant.query', 'example_manifest/assistant.ResearchAssistant.get_connection']
- decorator_list: []
- type_params: []
- docstring: Central class to help Research Analytics team members with their work.

ResearchAssistant is a "facade", i.e. it provides a simple interface to a
more-complex backend.
As such, methods belonging to ResearchAssistant should...
- Be the primary way any functionality in ra_lib is used
- Should have have names, arguments, and return values that are as static as possible.
Following these guidelines will help maintain the stability of ra_lib,
even when the internal code changes.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 646


#### example_manifest/assistant.ResearchAssistant.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/assistant.ResearchAssistant.__init__
- body: ['example_manifest/assistant.ResearchAssistant.__init__', 'example_manifest/assistant.ResearchAssistant.__init__', 'example_manifest/assistant.ResearchAssistant.__init__.0', 'example_manifest/assistant.ResearchAssistant.__init__.1', 'example_manifest/assistant.ResearchAssistant.__init__.2', 'example_manifest/assistant.ResearchAssistant.__init__.3', 'example_manifest/assistant.ResearchAssistant.__init__.4', 'example_manifest/assistant.ResearchAssistant.__init__.5', 'example_manifest/assistant.ResearchAssistant.__init__.6', 'example_manifest/assistant.ResearchAssistant.__init__.7', 'example_manifest/assistant.ResearchAssistant.__init__.8', 'example_manifest/assistant.ResearchAssistant.__init__.11', 'example_manifest/assistant.ResearchAssistant.__init__.11', 'example_manifest/assistant.ResearchAssistant.__init__.12']
- decorator_list: []
- type_params: []
- docstring: Constructor for Assistant.

Note to ra_lib developers: If we want to make it easier to create custom
versions of ResearchAssistant, we can always create a classmethod
ResearchAssistant.from_config that parses a config and creates
the ResearchAssistant accordingly.

Parameters
----------
report_id : str, optional
    Each assistant is created to help with a specific request. The
    report_id identifies that request. Default is None, which has the
    ResearchAssistant retrieve it automatically.
environment_settings : dict, optional
    Non-default settings passed to environment.EnvironmentSystem.
    EnvironmentSystem helps with handling the navigating the
    Databricks workspaces and changing settings accordingly.
    EnvironmentSystem assumes the user is working in a notebook environment.
cohort_settings : dict, optional
    Non-default settings passed to cohort.CohortSystem.
    CohortSystem helps work with cohorts, the group of patients associated
    with a study. Not all reports have cohorts, but it is very common.
query_settings : dict, optional
    Non-default settings passed to query.QuerySystem.
    QuerySystem helps with querying the data. In general Databricks' default
    functionality should be strongly preferred over using QuerySystem.
    QuerySystem's strength is working with on-prem data and blending it
    with cloud data.
azdo_settings : dict, optional
    Non-default settings passed to azdo.AzDOSystem.
    AzDOSystem is an interface to easily work programmatically with
    Azure Dev Ops.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 647


#### example_manifest/assistant.ResearchAssistant.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 648


#### example_manifest/assistant.ResearchAssistant.__init__.1

**Call:**
- func: environment.EnvironmentSystem
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 649


#### example_manifest/assistant.ResearchAssistant.__init__.10

**Call:**
- func: query.OnPremQuerySystem
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.__init__.10']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 650


#### example_manifest/assistant.ResearchAssistant.__init__.11

**Call:**
- func: self.environment_sys.warn
- args: ['example_manifest/assistant.ResearchAssistant.__init__.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 651


#### example_manifest/assistant.ResearchAssistant.__init__.12

**Call:**
- func: azdo.AzDOSystem
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.__init__.12', 'example_manifest/assistant.ResearchAssistant.__init__.12']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 652


#### example_manifest/assistant.ResearchAssistant.__init__.13

**Call:**
- func: self.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.13']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 653


#### example_manifest/assistant.ResearchAssistant.__init__.14

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.__init__.14']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 654


#### example_manifest/assistant.ResearchAssistant.__init__.2

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 655


#### example_manifest/assistant.ResearchAssistant.__init__.3

**Call:**
- func: utils.UtilsSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 656


#### example_manifest/assistant.ResearchAssistant.__init__.4

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 657


#### example_manifest/assistant.ResearchAssistant.__init__.5

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 658


#### example_manifest/assistant.ResearchAssistant.__init__.6

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.6', 'reports_config_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 659


#### example_manifest/assistant.ResearchAssistant.__init__.7

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.7', 'reports_schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 660


#### example_manifest/assistant.ResearchAssistant.__init__.8

**Call:**
- func: cohort.CohortSystem
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.__init__.8', 'example_manifest/assistant.ResearchAssistant.__init__.8']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 661


#### example_manifest/assistant.ResearchAssistant.__init__.9

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.__init__.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 662


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns

**FunctionDef:**
- name: add_report_dir_patterns
- args: example_manifest/assistant.ResearchAssistant.add_report_dir_patterns
- body: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.0']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 663


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.0

**Call:**
- func: reports_config.apply
- args: ['get_report_dir_pattern']
- keywords: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 664


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern

**FunctionDef:**
- name: get_report_dir_pattern
- args: example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern
- body: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.1', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.3', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5']
- decorator_list: []
- returns: str
- type_params: []
- docstring: This is applied on a per-row basis to get the report pattern.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 665


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.0

**Call:**
- func: self.utils_sys.sanitize_dirname
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 666


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.1

**Call:**
- func: self.utils_sys.sanitize_dirname
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 667


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.2

**Call:**
- func: pd.isna
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 668


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.3

**Call:**
- func: self.utils_sys.sanitize_dirname
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 669


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.4

**Call:**
- func: pd.isna
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 670


#### example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5.replace
- args: ['example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5', 'example_manifest/assistant.ResearchAssistant.add_report_dir_patterns.get_report_dir_pattern.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 671


#### example_manifest/assistant.ResearchAssistant.add_report_ids

**FunctionDef:**
- name: add_report_ids
- args: example_manifest/assistant.ResearchAssistant.add_report_ids
- body: ['example_manifest/assistant.ResearchAssistant.add_report_ids', 'example_manifest/assistant.ResearchAssistant.add_report_ids', 'example_manifest/assistant.ResearchAssistant.add_report_ids.1', 'example_manifest/assistant.ResearchAssistant.add_report_ids.2', 'example_manifest/assistant.ResearchAssistant.add_report_ids.3', 'example_manifest/assistant.ResearchAssistant.add_report_ids.4', 'example_manifest/assistant.ResearchAssistant.add_report_ids.4', 'example_manifest/assistant.ResearchAssistant.add_report_ids.4', 'example_manifest/assistant.ResearchAssistant.add_report_ids.4', 'example_manifest/assistant.ResearchAssistant.add_report_ids.5', 'example_manifest/assistant.ResearchAssistant.add_report_ids.6', 'example_manifest/assistant.ResearchAssistant.add_report_ids.7.0.0', 'example_manifest/assistant.ResearchAssistant.add_report_ids.8', 'example_manifest/assistant.ResearchAssistant.add_report_ids.8', 'example_manifest/assistant.ResearchAssistant.add_report_ids.8', 'example_manifest/assistant.ResearchAssistant.add_report_ids.9', 'example_manifest/assistant.ResearchAssistant.add_report_ids.10', 'example_manifest/assistant.ResearchAssistant.add_report_ids.12.0.0']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []
- docstring: Update the reports_config dataframe with the report_id.
        

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 672


#### example_manifest/assistant.ResearchAssistant.add_report_ids.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.0.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 673


#### example_manifest/assistant.ResearchAssistant.add_report_ids.1

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.1.isin
- args: ['reports_config.index']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 674


#### example_manifest/assistant.ResearchAssistant.add_report_ids.10

**Call:**
- func: nx.from_pandas_edgelist
- args: ['updated_report_wis']
- keywords: ['example_manifest/assistant.ResearchAssistant.add_report_ids.10', 'example_manifest/assistant.ResearchAssistant.add_report_ids.10']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 675


#### example_manifest/assistant.ResearchAssistant.add_report_ids.11

**Call:**
- func: nx.connected_components
- args: ['g']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 676


#### example_manifest/assistant.ResearchAssistant.add_report_ids.12

**Call:**
- func: np.array
- args: ['example_manifest/assistant.ResearchAssistant.add_report_ids.12.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 677


#### example_manifest/assistant.ResearchAssistant.add_report_ids.12.0

**Call:**
- func: sorted
- args: ['example_manifest/assistant.ResearchAssistant.add_report_ids.12.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 678


#### example_manifest/assistant.ResearchAssistant.add_report_ids.12.0.0

**Call:**
- func: list
- args: ['component']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 679


#### example_manifest/assistant.ResearchAssistant.add_report_ids.2

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.2.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 680


#### example_manifest/assistant.ResearchAssistant.add_report_ids.3

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.3.apply
- args: ['example_manifest/assistant.ResearchAssistant.add_report_ids.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 681


#### example_manifest/assistant.ResearchAssistant.add_report_ids.4

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.4.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 682


#### example_manifest/assistant.ResearchAssistant.add_report_ids.5

**Call:**
- func: has_invalid_irb.any
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 683


#### example_manifest/assistant.ResearchAssistant.add_report_ids.6

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.6.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 684


#### example_manifest/assistant.ResearchAssistant.add_report_ids.7

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.7.0.astype
- args: ['int']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 685


#### example_manifest/assistant.ResearchAssistant.add_report_ids.7.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.7.0.rank
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 686


#### example_manifest/assistant.ResearchAssistant.add_report_ids.7.0.0

**Call:**
- func: irb_reports.groupby
- args: ['example_manifest/assistant.ResearchAssistant.add_report_ids.7.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 687


#### example_manifest/assistant.ResearchAssistant.add_report_ids.8

**Call:**
- func: irb_reports.apply
- args: ['example_manifest/assistant.ResearchAssistant.add_report_ids.8']
- keywords: ['example_manifest/assistant.ResearchAssistant.add_report_ids.8']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 688


#### example_manifest/assistant.ResearchAssistant.add_report_ids.9

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_ids.9.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 689


#### example_manifest/assistant.ResearchAssistant.add_report_locations

**FunctionDef:**
- name: add_report_locations
- args: example_manifest/assistant.ResearchAssistant.add_report_locations
- body: ['example_manifest/assistant.ResearchAssistant.add_report_locations', 'example_manifest/assistant.ResearchAssistant.add_report_locations', 'example_manifest/assistant.ResearchAssistant.add_report_locations.0.0', 'example_manifest/assistant.ResearchAssistant.add_report_locations.1', 'example_manifest/assistant.ResearchAssistant.add_report_locations.1', 'example_manifest/assistant.ResearchAssistant.add_report_locations.1', 'example_manifest/assistant.ResearchAssistant.add_report_locations.2', 'example_manifest/assistant.ResearchAssistant.add_report_locations.3']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 690


#### example_manifest/assistant.ResearchAssistant.add_report_locations.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_locations.0.0.all
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.add_report_locations.0.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 691


#### example_manifest/assistant.ResearchAssistant.add_report_locations.0.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_locations.0.0.isna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 692


#### example_manifest/assistant.ResearchAssistant.add_report_locations.1

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_locations.1.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 693


#### example_manifest/assistant.ResearchAssistant.add_report_locations.2

**Call:**
- func: self.get_valid_report_locations
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 694


#### example_manifest/assistant.ResearchAssistant.add_report_locations.3

**Call:**
- func: example_manifest/assistant.ResearchAssistant.add_report_locations.3.isin
- args: ['example_manifest/assistant.ResearchAssistant.add_report_locations.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 695


#### example_manifest/assistant.ResearchAssistant.build_report_structure

**FunctionDef:**
- name: build_report_structure
- args: example_manifest/assistant.ResearchAssistant.build_report_structure
- body: ['example_manifest/assistant.ResearchAssistant.build_report_structure', 'example_manifest/assistant.ResearchAssistant.build_report_structure.0', 'example_manifest/assistant.ResearchAssistant.build_report_structure.1', 'example_manifest/assistant.ResearchAssistant.build_report_structure.2', 'example_manifest/assistant.ResearchAssistant.build_report_structure.3', 'example_manifest/assistant.ResearchAssistant.build_report_structure.4', 'example_manifest/assistant.ResearchAssistant.build_report_structure.5', 'example_manifest/assistant.ResearchAssistant.build_report_structure.5', 'example_manifest/assistant.ResearchAssistant.build_report_structure.12']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 696


#### example_manifest/assistant.ResearchAssistant.build_report_structure.0

**Call:**
- func: WorkspaceClient
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 697


#### example_manifest/assistant.ResearchAssistant.build_report_structure.1

**Call:**
- func: os.path.abspath
- args: ['report_dir']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 698


#### example_manifest/assistant.ResearchAssistant.build_report_structure.10

**Call:**
- func: os.path.basename
- args: ['report_file_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 699


#### example_manifest/assistant.ResearchAssistant.build_report_structure.11

**Call:**
- func: w.workspace.import_
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.build_report_structure.11', 'example_manifest/assistant.ResearchAssistant.build_report_structure.11', 'example_manifest/assistant.ResearchAssistant.build_report_structure.11', 'example_manifest/assistant.ResearchAssistant.build_report_structure.11']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 700


#### example_manifest/assistant.ResearchAssistant.build_report_structure.12

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.build_report_structure.12']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 701


#### example_manifest/assistant.ResearchAssistant.build_report_structure.13

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.build_report_structure.13']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 702


#### example_manifest/assistant.ResearchAssistant.build_report_structure.2

**Call:**
- func: os.path.abspath
- args: ['template_dir']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 703


#### example_manifest/assistant.ResearchAssistant.build_report_structure.3

**Call:**
- func: os.path.abspath
- args: ['ra_lib_setup_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 704


#### example_manifest/assistant.ResearchAssistant.build_report_structure.4

**Call:**
- func: os.path.relpath
- args: ['ra_lib_setup_path']
- keywords: ['example_manifest/assistant.ResearchAssistant.build_report_structure.4']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 705


#### example_manifest/assistant.ResearchAssistant.build_report_structure.5

**Call:**
- func: os.makedirs
- args: ['report_dir']
- keywords: ['example_manifest/assistant.ResearchAssistant.build_report_structure.5']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 706


#### example_manifest/assistant.ResearchAssistant.build_report_structure.6

**Call:**
- func: w.workspace.export
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.build_report_structure.6', 'example_manifest/assistant.ResearchAssistant.build_report_structure.6']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 707


#### example_manifest/assistant.ResearchAssistant.build_report_structure.7

**Call:**
- func: example_manifest/assistant.ResearchAssistant.build_report_structure.7.0.decode
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 708


#### example_manifest/assistant.ResearchAssistant.build_report_structure.7.0

**Call:**
- func: base64.b64decode
- args: ['export_response.content']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 709


#### example_manifest/assistant.ResearchAssistant.build_report_structure.8

**Call:**
- func: notebook_str.replace
- args: ['str_to_replace', 'relative_ra_lib_setup_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 710


#### example_manifest/assistant.ResearchAssistant.build_report_structure.9

**Call:**
- func: example_manifest/assistant.ResearchAssistant.build_report_structure.9.0.decode
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 711


#### example_manifest/assistant.ResearchAssistant.build_report_structure.9.0

**Call:**
- func: base64.b64encode
- args: ['example_manifest/assistant.ResearchAssistant.build_report_structure.9.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 712


#### example_manifest/assistant.ResearchAssistant.build_report_structure.9.0.0

**Call:**
- func: modified_notebook_str.encode
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 713


#### example_manifest/assistant.ResearchAssistant.draft_report_structure

**FunctionDef:**
- name: draft_report_structure
- args: example_manifest/assistant.ResearchAssistant.draft_report_structure
- body: ['example_manifest/assistant.ResearchAssistant.draft_report_structure', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.0', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.0', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.0', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.1', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.1', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.2', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.4', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.5', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.6', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.6']
- decorator_list: []
- returns: dict
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 714


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.0

**Call:**
- func: pd.isna
- args: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 715


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.1

**Call:**
- func: self.utils_sys.sanitize_dirname
- args: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.1']
- keywords: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 716


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.2

**Call:**
- func: example_manifest/assistant.ResearchAssistant.draft_report_structure.2.replace
- args: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.2', 'example_manifest/assistant.ResearchAssistant.draft_report_structure.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 717


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.3

**Call:**
- func: report_dir_str.format
- args: ['study_dir_label', 'report_dir_label']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 718


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.4

**Call:**
- func: report_dir_str.format
- args: ['report_dir_label']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 719


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.5

**Call:**
- func: os.path.abspath
- args: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 720


#### example_manifest/assistant.ResearchAssistant.draft_report_structure.6

**Call:**
- func: report_files.append
- args: ['example_manifest/assistant.ResearchAssistant.draft_report_structure.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 721


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config

**FunctionDef:**
- name: finalize_reports_config
- args: example_manifest/assistant.ResearchAssistant.finalize_reports_config
- body: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.1', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.1', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.1', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.2.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.3', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.5', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.6', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.7.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.9']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 722


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.0.apply
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 723


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.1

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.1.isna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 724


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.2

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.2.0.astype
- args: ['bool']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 725


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.2.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.2.0.fillna
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 726


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.3

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 727


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.4

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.idxmax
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 728


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0.groupby
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 729


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0

**Call:**
- func: reports_config.query
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.4.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 730


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.5

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.5.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 731


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.6

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 732


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.7

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.7.0.filter
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.7.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 733


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.7.0

**Call:**
- func: self.spark.table
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.7.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 734


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.8

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 735


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.toPandas
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 736


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0

**Call:**
- func: reports_irbs.join
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0']
- keywords: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0', 'example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 737


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0

**Call:**
- func: studies.select
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.8.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 738


#### example_manifest/assistant.ResearchAssistant.finalize_reports_config.9

**Call:**
- func: reports_config.sort_values
- args: ['example_manifest/assistant.ResearchAssistant.finalize_reports_config.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 739


#### example_manifest/assistant.ResearchAssistant.generate_reports_config

**FunctionDef:**
- name: generate_reports_config
- args: example_manifest/assistant.ResearchAssistant.generate_reports_config
- body: ['example_manifest/assistant.ResearchAssistant.generate_reports_config', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.0', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.1', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.2', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.3', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.4', 'example_manifest/assistant.ResearchAssistant.generate_reports_config.5']
- decorator_list: []
- returns: example_manifest/assistant.ResearchAssistant.generate_reports_config.5
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 740


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.0

**Call:**
- func: self.get_reports_config_base
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 741


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.1

**Call:**
- func: self.add_report_ids
- args: ['reports_config']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 742


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.2

**Call:**
- func: self.add_report_locations
- args: ['reports_config']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 743


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.3

**Call:**
- func: self.add_report_dir_patterns
- args: ['reports_config']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 744


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.4

**Call:**
- func: self.finalize_reports_config
- args: ['reports_config']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 745


#### example_manifest/assistant.ResearchAssistant.generate_reports_config.5

**Call:**
- func: self.write_reports_config
- args: ['reports_config']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 746


#### example_manifest/assistant.ResearchAssistant.get

**FunctionDef:**
- name: get
- args: example_manifest/assistant.ResearchAssistant.get
- body: ['example_manifest/assistant.ResearchAssistant.get']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 747


#### example_manifest/assistant.ResearchAssistant.get.0

**Call:**
- func: self.environment_sys.get
- args: ['key', 'example_manifest/assistant.ResearchAssistant.get.0']
- keywords: ['example_manifest/assistant.ResearchAssistant.get.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 748


#### example_manifest/assistant.ResearchAssistant.get_connection

**FunctionDef:**
- name: get_connection
- args: example_manifest/assistant.ResearchAssistant.get_connection
- body: ['example_manifest/assistant.ResearchAssistant.get_connection']
- decorator_list: []
- returns: sqlalchemy.engine.base.Connection
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 749


#### example_manifest/assistant.ResearchAssistant.get_connection.0

**Call:**
- func: self.query_sys.get_open_connection
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 750


#### example_manifest/assistant.ResearchAssistant.get_report_config

**FunctionDef:**
- name: get_report_config
- args: example_manifest/assistant.ResearchAssistant.get_report_config
- body: ['example_manifest/assistant.ResearchAssistant.get_report_config', 'example_manifest/assistant.ResearchAssistant.get_report_config.0', 'example_manifest/assistant.ResearchAssistant.get_report_config.1', 'example_manifest/assistant.ResearchAssistant.get_report_config.1', 'example_manifest/assistant.ResearchAssistant.get_report_config.3']
- decorator_list: []
- returns: pd.Series
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 751


#### example_manifest/assistant.ResearchAssistant.get_report_config.0

**Call:**
- func: time.time
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 752


#### example_manifest/assistant.ResearchAssistant.get_report_config.1

**Call:**
- func: self.generate_reports_config
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 753


#### example_manifest/assistant.ResearchAssistant.get_report_config.2

**Call:**
- func: time.time
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 754


#### example_manifest/assistant.ResearchAssistant.get_report_config.3

**Call:**
- func: self.environment_sys.warn
- args: ['example_manifest/assistant.ResearchAssistant.get_report_config.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 755


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base

**FunctionDef:**
- name: get_reports_config_base
- args: example_manifest/assistant.ResearchAssistant.get_reports_config_base
- body: ['example_manifest/assistant.ResearchAssistant.get_reports_config_base', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base.0', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base.0', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base.0', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base.1', 'example_manifest/assistant.ResearchAssistant.get_reports_config_base.2.0']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 756


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base.0

**Call:**
- func: self.azdo_sys.get_report_work_items
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 757


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base.1

**Call:**
- func: report_work_items.rename
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.get_reports_config_base.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 758


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base.2

**Call:**
- func: list
- args: ['example_manifest/assistant.ResearchAssistant.get_reports_config_base.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 759


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base.2.0

**Call:**
- func: renamed_azdo_columns.values
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 760


#### example_manifest/assistant.ResearchAssistant.get_reports_config_base.3

**Call:**
- func: reports_config.set_index
- args: ['example_manifest/assistant.ResearchAssistant.get_reports_config_base.3']
- keywords: ['example_manifest/assistant.ResearchAssistant.get_reports_config_base.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 761


#### example_manifest/assistant.ResearchAssistant.get_valid_report_locations

**FunctionDef:**
- name: get_valid_report_locations
- args: example_manifest/assistant.ResearchAssistant.get_valid_report_locations
- body: ['example_manifest/assistant.ResearchAssistant.get_valid_report_locations', 'example_manifest/assistant.ResearchAssistant.get_valid_report_locations', 'example_manifest/assistant.ResearchAssistant.get_valid_report_locations.0']
- decorator_list: []
- type_params: []
- docstring: This is turned into a function so we can have easier access for reference.
        

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 762


#### example_manifest/assistant.ResearchAssistant.get_valid_report_locations.0

**Call:**
- func: os.path.dirname
- args: ['__file__']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 763


#### example_manifest/assistant.ResearchAssistant.get_valid_report_locations.1

**Call:**
- func: pd.read_csv
- args: ['workspaces_fp']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 764


#### example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh

**FunctionDef:**
- name: identify_reports_to_refresh
- args: example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh
- body: ['example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh', 'example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh']
- decorator_list: []
- type_params: []
- docstring: Metadata
--------
- satisfies: can_control_refresh_frequency
- status: new

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**link:**
- source: example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh
- target: can_control_refresh_frequency
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### example_manifest/assistant.ResearchAssistant.identify_reports_to_refresh.0

**Call:**
- func: NotImplementedError
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 765


#### example_manifest/assistant.ResearchAssistant.load_cohort

**FunctionDef:**
- name: load_cohort
- args: example_manifest/assistant.ResearchAssistant.load_cohort
- body: ['example_manifest/assistant.ResearchAssistant.load_cohort', 'example_manifest/assistant.ResearchAssistant.load_cohort']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 766


#### example_manifest/assistant.ResearchAssistant.load_cohort.0

**Call:**
- func: self.cohort_sys.load_cohort
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.load_cohort.0', 'example_manifest/assistant.ResearchAssistant.load_cohort.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 767


#### example_manifest/assistant.ResearchAssistant.query

**FunctionDef:**
- name: query
- args: example_manifest/assistant.ResearchAssistant.query
- body: ['example_manifest/assistant.ResearchAssistant.query', 'example_manifest/assistant.ResearchAssistant.query.0']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 768


#### example_manifest/assistant.ResearchAssistant.query.0

**Call:**
- func: ValueError
- args: ['example_manifest/assistant.ResearchAssistant.query.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 769


#### example_manifest/assistant.ResearchAssistant.query.1

**Call:**
- func: self.query_sys.query
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.query.1', 'example_manifest/assistant.ResearchAssistant.query.1', 'example_manifest/assistant.ResearchAssistant.query.1', 'example_manifest/assistant.ResearchAssistant.query.1', 'example_manifest/assistant.ResearchAssistant.query.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 770


#### example_manifest/assistant.ResearchAssistant.save_cohort

**FunctionDef:**
- name: save_cohort
- args: example_manifest/assistant.ResearchAssistant.save_cohort
- body: ['example_manifest/assistant.ResearchAssistant.save_cohort', 'example_manifest/assistant.ResearchAssistant.save_cohort']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 771


#### example_manifest/assistant.ResearchAssistant.save_cohort.0

**Call:**
- func: self.cohort_sys.write_cohort
- args: []
- keywords: ['example_manifest/assistant.ResearchAssistant.save_cohort.0', 'example_manifest/assistant.ResearchAssistant.save_cohort.0', 'example_manifest/assistant.ResearchAssistant.save_cohort.0', 'example_manifest/assistant.ResearchAssistant.save_cohort.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 772


#### example_manifest/assistant.ResearchAssistant.save_report_table

**FunctionDef:**
- name: save_report_table
- args: example_manifest/assistant.ResearchAssistant.save_report_table
- body: ['example_manifest/assistant.ResearchAssistant.save_report_table', 'example_manifest/assistant.ResearchAssistant.save_report_table.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.2', 'example_manifest/assistant.ResearchAssistant.save_report_table.4', 'example_manifest/assistant.ResearchAssistant.save_report_table.5.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 773


#### example_manifest/assistant.ResearchAssistant.save_report_table.0

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 774


#### example_manifest/assistant.ResearchAssistant.save_report_table.1

**Call:**
- func: example_manifest/assistant.ResearchAssistant.save_report_table.1.0.replace
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 775


#### example_manifest/assistant.ResearchAssistant.save_report_table.1.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0.replace
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 776


#### example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0

**Call:**
- func: report_id.replace
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.1.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 777


#### example_manifest/assistant.ResearchAssistant.save_report_table.2

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 778


#### example_manifest/assistant.ResearchAssistant.save_report_table.3

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 779


#### example_manifest/assistant.ResearchAssistant.save_report_table.4

**Call:**
- func: self.spark.table
- args: ['view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 780


#### example_manifest/assistant.ResearchAssistant.save_report_table.5

**Call:**
- func: report_df.withColumn
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.5', 'example_manifest/assistant.ResearchAssistant.save_report_table.5.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 781


#### example_manifest/assistant.ResearchAssistant.save_report_table.5.0

**Call:**
- func: lit
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 782


#### example_manifest/assistant.ResearchAssistant.save_report_table.6

**Call:**
- func: example_manifest/assistant.ResearchAssistant.save_report_table.6.0.saveAsTable
- args: ['table_path']
- keywords: ['example_manifest/assistant.ResearchAssistant.save_report_table.6.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.6.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 783


#### example_manifest/assistant.ResearchAssistant.save_report_table.6.0

**Call:**
- func: report_df.write.option
- args: ['example_manifest/assistant.ResearchAssistant.save_report_table.6.0', 'example_manifest/assistant.ResearchAssistant.save_report_table.6.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 784


#### example_manifest/assistant.ResearchAssistant.set

**FunctionDef:**
- name: set
- args: example_manifest/assistant.ResearchAssistant.set
- body: ['example_manifest/assistant.ResearchAssistant.set']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 785


#### example_manifest/assistant.ResearchAssistant.set.0

**Call:**
- func: self.environment_sys.set
- args: ['key', 'value']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 786


#### example_manifest/assistant.ResearchAssistant.write_reports_config

**FunctionDef:**
- name: write_reports_config
- args: example_manifest/assistant.ResearchAssistant.write_reports_config
- body: ['example_manifest/assistant.ResearchAssistant.write_reports_config', 'example_manifest/assistant.ResearchAssistant.write_reports_config', 'example_manifest/assistant.ResearchAssistant.write_reports_config.0', 'example_manifest/assistant.ResearchAssistant.write_reports_config.1', 'example_manifest/assistant.ResearchAssistant.write_reports_config.2.0', 'example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.0', 'example_manifest/assistant.ResearchAssistant.write_reports_config.4']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: Note: A function to build a specific table would not normally be incorporated into ra_lib.
However, because so much of ra_lib revolves around the config table we include and test it
as part of ra_lib.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 787


#### example_manifest/assistant.ResearchAssistant.write_reports_config.0

**Call:**
- func: self.spark.sql
- args: ['example_manifest/assistant.ResearchAssistant.write_reports_config.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 788


#### example_manifest/assistant.ResearchAssistant.write_reports_config.1

**Call:**
- func: self.spark.sql
- args: ['example_manifest/assistant.ResearchAssistant.write_reports_config.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 789


#### example_manifest/assistant.ResearchAssistant.write_reports_config.2

**Call:**
- func: self.utils_sys.create_matching_dataframe
- args: ['reports_config', 'example_manifest/assistant.ResearchAssistant.write_reports_config.2.0.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 790


#### example_manifest/assistant.ResearchAssistant.write_reports_config.2.0

**Call:**
- func: self.spark.table
- args: ['self.reports_config_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 791


#### example_manifest/assistant.ResearchAssistant.write_reports_config.3

**Call:**
- func: example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.saveAsTable
- args: ['self.reports_config_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 792


#### example_manifest/assistant.ResearchAssistant.write_reports_config.3.0

**Call:**
- func: example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.0.mode
- args: ['example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 793


#### example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.0

**Call:**
- func: reports_config_spark.write.format
- args: ['example_manifest/assistant.ResearchAssistant.write_reports_config.3.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 794


#### example_manifest/assistant.ResearchAssistant.write_reports_config.4

**Call:**
- func: print
- args: ['example_manifest/assistant.ResearchAssistant.write_reports_config.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 795


#### example_manifest/assistant.ResearchAssistant.write_reports_config.5

**Call:**
- func: self.spark.table
- args: ['self.reports_config_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/assistant.py

**node:**
- connected_component_group: 796


#### example_manifest/azdo

**Module:**
- body: ['example_manifest/azdo.0', 'example_manifest/azdo.1', 'example_manifest/azdo.2', 'example_manifest/azdo.3', 'example_manifest/azdo.4', 'example_manifest/azdo.5', 'example_manifest/azdo.6', 'example_manifest/azdo.7', 'example_manifest/azdo.8', 'example_manifest/azdo.9', 'example_manifest/azdo.10', 'example_manifest/azdo.11', 'example_manifest/azdo.12', 'example_manifest/azdo.13', 'example_manifest/azdo.13', 'example_manifest/azdo.AzDOSystem']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 797


#### example_manifest/azdo.0

**Import:**
- names: [{'name': 'os', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 798


#### example_manifest/azdo.1

**Import:**
- names: [{'name': 're', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 799


#### example_manifest/azdo.10

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 800


#### example_manifest/azdo.11

**ImportFrom:**
- module: pyspark.sql.dataframe
- names: [{'name': 'DataFrame', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 801


#### example_manifest/azdo.12

**ImportFrom:**
- module: environment
- names: [{'name': 'EnvironmentSystem', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 802


#### example_manifest/azdo.13

**ImportFrom:**
- module: utils
- names: [{'name': 'UtilsSystem', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 803


#### example_manifest/azdo.2

**ImportFrom:**
- module: azure.devops.connection
- names: [{'name': 'Connection', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 804


#### example_manifest/azdo.3

**ImportFrom:**
- module: azure.devops.exceptions
- names: [{'name': 'AzureDevOpsServiceError', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 805


#### example_manifest/azdo.4

**ImportFrom:**
- module: azure.devops.v7_0.work_item_tracking.models
- names: [{'name': 'Wiql', 'asname': None}, {'name': 'TeamContext', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 806


#### example_manifest/azdo.5

**ImportFrom:**
- module: msrest.authentication
- names: [{'name': 'BasicAuthentication', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 807


#### example_manifest/azdo.6

**Import:**
- names: [{'name': 'numpy', 'asname': 'np'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 808


#### example_manifest/azdo.7

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 809


#### example_manifest/azdo.8

**Import:**
- names: [{'name': 'tqdm', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 810


#### example_manifest/azdo.9

**Import:**
- names: [{'name': 'yaml', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 811


#### example_manifest/azdo.AzDOSystem

**ClassDef:**
- name: AzDOSystem
- bases: []
- keywords: []
- body: ['example_manifest/azdo.AzDOSystem.__init__', 'example_manifest/azdo.AzDOSystem.query', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items', 'example_manifest/azdo.AzDOSystem.get_work_items', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions', 'example_manifest/azdo.AzDOSystem.get_report_work_items']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 812


#### example_manifest/azdo.AzDOSystem.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/azdo.AzDOSystem.__init__
- body: ['example_manifest/azdo.AzDOSystem.__init__', 'example_manifest/azdo.AzDOSystem.__init__.0', 'example_manifest/azdo.AzDOSystem.__init__.1', 'example_manifest/azdo.AzDOSystem.__init__.2', 'example_manifest/azdo.AzDOSystem.__init__.3.0', 'example_manifest/azdo.AzDOSystem.__init__.4', 'example_manifest/azdo.AzDOSystem.__init__.5']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 813


#### example_manifest/azdo.AzDOSystem.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 814


#### example_manifest/azdo.AzDOSystem.__init__.1

**Call:**
- func: EnvironmentSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 815


#### example_manifest/azdo.AzDOSystem.__init__.2

**Call:**
- func: UtilsSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 816


#### example_manifest/azdo.AzDOSystem.__init__.3

**Call:**
- func: BasicAuthentication
- args: ['example_manifest/azdo.AzDOSystem.__init__.3', 'example_manifest/azdo.AzDOSystem.__init__.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 817


#### example_manifest/azdo.AzDOSystem.__init__.3.0

**Call:**
- func: self.environment_sys.get_secret
- args: ['example_manifest/azdo.AzDOSystem.__init__.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 818


#### example_manifest/azdo.AzDOSystem.__init__.4

**Call:**
- func: Connection
- args: []
- keywords: ['example_manifest/azdo.AzDOSystem.__init__.4', 'example_manifest/azdo.AzDOSystem.__init__.4']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 819


#### example_manifest/azdo.AzDOSystem.__init__.5

**Call:**
- func: self.connection.clients.get_work_item_tracking_client
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 820


#### example_manifest/azdo.AzDOSystem.__init__.6

**Call:**
- func: TeamContext
- args: ['team']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 821


#### example_manifest/azdo.AzDOSystem.get_report_work_items

**FunctionDef:**
- name: get_report_work_items
- args: example_manifest/azdo.AzDOSystem.get_report_work_items
- body: ['example_manifest/azdo.AzDOSystem.get_report_work_items', 'example_manifest/azdo.AzDOSystem.get_report_work_items']
- decorator_list: []
- type_params: []
- docstring: The query used to identify reports.
        

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 822


#### example_manifest/azdo.AzDOSystem.get_report_work_items.0

**Call:**
- func: self.get_work_items
- args: []
- keywords: ['example_manifest/azdo.AzDOSystem.get_report_work_items.0', 'example_manifest/azdo.AzDOSystem.get_report_work_items.0', 'example_manifest/azdo.AzDOSystem.get_report_work_items.0', 'example_manifest/azdo.AzDOSystem.get_report_work_items.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 823


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items

**FunctionDef:**
- name: get_unparsed_work_items
- args: example_manifest/azdo.AzDOSystem.get_unparsed_work_items
- body: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.1', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.1', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.1', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.10', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.11']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []
- docstring: Get a pandas dataframe containing queried work items.
This works by doing two separate queries: one that gets the IDs,
and a second that gets the fields.

Parameters
----------
wiql_query : str
    A query for the work items. Should only select [System.Id].

fields : list[str]
    The specified fields to return.

Returns
-------
pd.DataFrame
    The pandas dataframe of work items.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 824


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.0

**Call:**
- func: isinstance
- args: ['wi_selection', 'list']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 825


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.1

**Call:**
- func: self.query
- args: ['wi_selection']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 826


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.10

**Call:**
- func: work_items.append
- args: ['work_item']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 827


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.11

**Call:**
- func: pd.DataFrame
- args: ['work_items']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 828


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.2

**Call:**
- func: enumerate
- args: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 829


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.2.0

**Call:**
- func: tqdm.tqdm
- args: ['work_item_ids']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 830


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.3

**Call:**
- func: self.wit_client.get_work_item
- args: ['wi_id']
- keywords: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 831


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.4

**Call:**
- func: work_item_response.as_dict
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 832


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.5

**Call:**
- func: n_relation_type.setdefault
- args: ['relation_type', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 833


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.6

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_unparsed_work_items.6.split
- args: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 834


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.7

**Call:**
- func: int
- args: ['linked_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 835


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.8

**Call:**
- func: self.get_work_item_at_time
- args: ['wi_id']
- keywords: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items.8', 'example_manifest/azdo.AzDOSystem.get_unparsed_work_items.8']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 836


#### example_manifest/azdo.AzDOSystem.get_unparsed_work_items.9

**Call:**
- func: NotImplementedError
- args: ['example_manifest/azdo.AzDOSystem.get_unparsed_work_items.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 837


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time

**FunctionDef:**
- name: get_work_item_at_time
- args: example_manifest/azdo.AzDOSystem.get_work_item_at_time
- body: ['example_manifest/azdo.AzDOSystem.get_work_item_at_time', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time.1', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time.1', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time.7']
- decorator_list: []
- returns: dict
- type_params: []
- docstring: This can probably be deprecated--the Python api offers the "as_of" argument.
        

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 838


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.0

**Call:**
- func: isinstance
- args: ['time', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 839


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.1

**Call:**
- func: pd.Timestamp
- args: ['time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 840


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.2

**Call:**
- func: enumerate
- args: ['example_manifest/azdo.AzDOSystem.get_work_item_at_time.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 841


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.2.0

**Call:**
- func: self.wit_client.get_updates
- args: ['wi_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 842


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.3

**Call:**
- func: update.as_dict
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 843


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.4

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_item_at_time.4.0.tz_localize
- args: ['example_manifest/azdo.AzDOSystem.get_work_item_at_time.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 844


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.4.0

**Call:**
- func: pd.Timestamp
- args: ['time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 845


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.5

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_item_at_time.5.0.tz_localize
- args: ['example_manifest/azdo.AzDOSystem.get_work_item_at_time.5.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 846


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.5.0

**Call:**
- func: pd.Timestamp
- args: ['update_time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 847


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.6

**Call:**
- func: work_item.setdefault
- args: ['field', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 848


#### example_manifest/azdo.AzDOSystem.get_work_item_at_time.7

**Call:**
- func: value.get
- args: ['example_manifest/azdo.AzDOSystem.get_work_item_at_time.7', 'example_manifest/azdo.AzDOSystem.get_work_item_at_time.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 849


#### example_manifest/azdo.AzDOSystem.get_work_items

**FunctionDef:**
- name: get_work_items
- args: example_manifest/azdo.AzDOSystem.get_work_items
- body: ['example_manifest/azdo.AzDOSystem.get_work_items', 'example_manifest/azdo.AzDOSystem.get_work_items', 'example_manifest/azdo.AzDOSystem.get_work_items.1', 'example_manifest/azdo.AzDOSystem.get_work_items.2', 'example_manifest/azdo.AzDOSystem.get_work_items.3', 'example_manifest/azdo.AzDOSystem.get_work_items.4.0', 'example_manifest/azdo.AzDOSystem.get_work_items.7', 'example_manifest/azdo.AzDOSystem.get_work_items.10.0', 'example_manifest/azdo.AzDOSystem.get_work_items.15', 'example_manifest/azdo.AzDOSystem.get_work_items.16', 'example_manifest/azdo.AzDOSystem.get_work_items.17']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []
- docstring: Get a pandas dataframe containing queried work items.
This is different from get_unparsed_work_items in that this call is cleaned up

Parameters
----------
wi_selection : str
    A query for the work items. Should only select [System.Id].

fields : list[str]
    The specified fields to return.

jitter_state_value: bool
    If True, then add random noise to the StateValue, useful for plotting.

join_self_for_parents: bool
    If True, join the dataframe to itself on ID = Parent.
    This is only sensible if the dataframe contains the parents.

parse_descriptions: bool
    If True, look for yaml-formatted data in the description and put the attributes into new columns.

Returns
-------
pd.DataFrame
    The pandas dataframe of work items.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 850


#### example_manifest/azdo.AzDOSystem.get_work_items.0

**Call:**
- func: isinstance
- args: ['wi_selection', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 851


#### example_manifest/azdo.AzDOSystem.get_work_items.1

**Call:**
- func: ValueError
- args: ['example_manifest/azdo.AzDOSystem.get_work_items.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 852


#### example_manifest/azdo.AzDOSystem.get_work_items.10

**Call:**
- func: rng.normal
- args: []
- keywords: ['example_manifest/azdo.AzDOSystem.get_work_items.10', 'example_manifest/azdo.AzDOSystem.get_work_items.10.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 853


#### example_manifest/azdo.AzDOSystem.get_work_items.10.0

**Call:**
- func: len
- args: ['work_items']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 854


#### example_manifest/azdo.AzDOSystem.get_work_items.11

**Call:**
- func: sprint_relativenumbers.items
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 855


#### example_manifest/azdo.AzDOSystem.get_work_items.12

**Call:**
- func: self.wit_client.query_by_wiql
- args: ['example_manifest/azdo.AzDOSystem.get_work_items.12.0']
- keywords: ['example_manifest/azdo.AzDOSystem.get_work_items.12.0', 'example_manifest/azdo.AzDOSystem.get_work_items.12.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 856


#### example_manifest/azdo.AzDOSystem.get_work_items.12.0

**Call:**
- func: Wiql
- args: ['query']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 857


#### example_manifest/azdo.AzDOSystem.get_work_items.13

**Call:**
- func: self.wit_client.get_work_item
- args: ['work_item_id']
- keywords: ['example_manifest/azdo.AzDOSystem.get_work_items.13']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 858


#### example_manifest/azdo.AzDOSystem.get_work_items.14

**Call:**
- func: work_item.as_dict
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 859


#### example_manifest/azdo.AzDOSystem.get_work_items.15

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.15.map
- args: ['sprints']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 860


#### example_manifest/azdo.AzDOSystem.get_work_items.16

**Call:**
- func: work_items.merge
- args: ['example_manifest/azdo.AzDOSystem.get_work_items.16']
- keywords: ['example_manifest/azdo.AzDOSystem.get_work_items.16', 'example_manifest/azdo.AzDOSystem.get_work_items.16', 'example_manifest/azdo.AzDOSystem.get_work_items.16', 'example_manifest/azdo.AzDOSystem.get_work_items.16']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 861


#### example_manifest/azdo.AzDOSystem.get_work_items.17

**Call:**
- func: self.parse_work_item_descriptions
- args: ['work_items']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 862


#### example_manifest/azdo.AzDOSystem.get_work_items.2

**Call:**
- func: self.get_unparsed_work_items
- args: ['wi_selection']
- keywords: ['example_manifest/azdo.AzDOSystem.get_work_items.2', 'example_manifest/azdo.AzDOSystem.get_work_items.2', 'example_manifest/azdo.AzDOSystem.get_work_items.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 863


#### example_manifest/azdo.AzDOSystem.get_work_items.3

**Call:**
- func: col.split
- args: ['example_manifest/azdo.AzDOSystem.get_work_items.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 864


#### example_manifest/azdo.AzDOSystem.get_work_items.4

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.4.0.sum
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 865


#### example_manifest/azdo.AzDOSystem.get_work_items.4.0

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.4.0.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 866


#### example_manifest/azdo.AzDOSystem.get_work_items.5

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.5.0.sum
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 867


#### example_manifest/azdo.AzDOSystem.get_work_items.5.0

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.5.0.notna
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 868


#### example_manifest/azdo.AzDOSystem.get_work_items.6

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.6.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 869


#### example_manifest/azdo.AzDOSystem.get_work_items.7

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.7.str.split
- args: ['example_manifest/azdo.AzDOSystem.get_work_items.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 870


#### example_manifest/azdo.AzDOSystem.get_work_items.8

**Call:**
- func: example_manifest/azdo.AzDOSystem.get_work_items.8.map
- args: ['state_values']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 871


#### example_manifest/azdo.AzDOSystem.get_work_items.9

**Call:**
- func: np.random.default_rng
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 872


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions

**FunctionDef:**
- name: parse_work_item_descriptions
- args: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions
- body: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.0', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.1', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.3', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.4', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.4', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.7', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.8']
- decorator_list: []
- returns: pd.DataFrame
- type_params: []
- docstring: The bottom of the description for some AzDO workitems is
yaml-formatted metadata.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 873


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.0

**Call:**
- func: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.0.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 874


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.1

**Call:**
- func: descriptions.str.replace
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.1', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.1']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 875


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.2

**Call:**
- func: descriptions.str.replace
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.2']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 876


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.3

**Call:**
- func: descriptions.str.replace
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.3', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.3']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 877


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.4

**Call:**
- func: descriptions.str.replace
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.4', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.4']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.4']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 878


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.5

**Call:**
- func: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.5.str.strip
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 879


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.5.0

**Call:**
- func: descriptions.str.rsplit
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.5.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 880


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.6

**Call:**
- func: descriptions.apply
- args: ['prune_whitespace']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 881


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.7

**Call:**
- func: work_items.apply
- args: ['load_yaml']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.7']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 882


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.8

**Call:**
- func: pd.json_normalize
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.8']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 883


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.9

**Call:**
- func: pd.concat
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.9']
- keywords: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.9']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 884


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml

**FunctionDef:**
- name: load_yaml
- args: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml
- body: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2']
- decorator_list: []
- type_params: []
- docstring: Function for safely loading yaml.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 885


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.0

**Call:**
- func: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.0.0.replace
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.0.0', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 886


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.0.0

**Call:**
- func: key.lower
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 887


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.1

**Call:**
- func: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.1.0.items
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 888


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.1.0

**Call:**
- func: yaml.safe_load
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 889


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.load_yaml.2

**Call:**
- func: repr
- args: ['e']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 890


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace

**FunctionDef:**
- name: prune_whitespace
- args: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace
- body: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.0', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.1', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.3']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 891


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.0

**Call:**
- func: isinstance
- args: ['text', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 892


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.1

**Call:**
- func: text.splitlines
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 893


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.2

**Call:**
- func: re.sub
- args: ['example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.2', 'example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 894


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.2.0

**Call:**
- func: line.strip
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 895


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.3

**Call:**
- func: line.strip
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 896


#### example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.4

**Call:**
- func: example_manifest/azdo.AzDOSystem.parse_work_item_descriptions.prune_whitespace.4.join
- args: ['cleaned_lines']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 897


#### example_manifest/azdo.AzDOSystem.query

**FunctionDef:**
- name: query
- args: example_manifest/azdo.AzDOSystem.query
- body: ['example_manifest/azdo.AzDOSystem.query', 'example_manifest/azdo.AzDOSystem.query.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 898


#### example_manifest/azdo.AzDOSystem.query.0

**Call:**
- func: Wiql
- args: []
- keywords: ['example_manifest/azdo.AzDOSystem.query.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 899


#### example_manifest/azdo.AzDOSystem.query.1

**Call:**
- func: self.wit_client.query_by_wiql
- args: ['wiql']
- keywords: ['example_manifest/azdo.AzDOSystem.query.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/azdo.py

**node:**
- connected_component_group: 900


#### example_manifest/cohort

**Module:**
- body: ['example_manifest/cohort.0', 'example_manifest/cohort.1', 'example_manifest/cohort.2', 'example_manifest/cohort.3', 'example_manifest/cohort.4', 'example_manifest/cohort.5', 'example_manifest/cohort.6', 'example_manifest/cohort.7', 'example_manifest/cohort.8', 'example_manifest/cohort.9', 'example_manifest/cohort.CohortSystem', 'example_manifest/cohort.ArrayCohortSystem', 'example_manifest/cohort.CohortMocker', 'example_manifest/cohort.CohortMocker.write_mock_data.2', 'example_manifest/cohort.CohortMocker.write_mock_data.2']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 901


#### example_manifest/cohort.0

**ImportFrom:**
- module: dataclasses
- names: [{'name': 'dataclass', 'asname': None}, {'name': 'field', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 902


#### example_manifest/cohort.1

**Import:**
- names: [{'name': 'numpy', 'asname': 'np'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 903


#### example_manifest/cohort.10

**Call:**
- func: pd.unique
- args: ['example_manifest/cohort.10.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 904


#### example_manifest/cohort.10.0

**Call:**
- func: list
- args: ['example_manifest/cohort.10.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 905


#### example_manifest/cohort.10.0.0

**Call:**
- func: ID_MAPPING.values
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 906


#### example_manifest/cohort.2

**Import:**
- names: [{'name': 'tqdm', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 907


#### example_manifest/cohort.3

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 908


#### example_manifest/cohort.4

**ImportFrom:**
- module: pyspark.sql.dataframe
- names: [{'name': 'DataFrame', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 909


#### example_manifest/cohort.5

**ImportFrom:**
- module: pyspark.sql.connect.dataframe
- names: [{'name': 'DataFrame', 'asname': 'ConnectDataFrame'}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 910


#### example_manifest/cohort.6

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 911


#### example_manifest/cohort.7

**ImportFrom:**
- module: pyspark.sql.functions
- names: [{'name': 'col', 'asname': None}, {'name': 'collect_list', 'asname': None}, {'name': 'explode', 'asname': None}, {'name': 'lit', 'asname': None}, {'name': 'max', 'asname': None}, {'name': 'when', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 912


#### example_manifest/cohort.8

**ImportFrom:**
- module: environment
- names: [{'name': 'EnvironmentSystem', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 913


#### example_manifest/cohort.9

**ImportFrom:**
- module: utils
- names: [{'name': 'UtilsSystem', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 914


#### example_manifest/cohort.ArrayCohortSystem

**ClassDef:**
- name: ArrayCohortSystem
- bases: ['CohortSystem']
- keywords: []
- body: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients', 'example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history', 'example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables', 'example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write', 'example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 915


#### example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients

**FunctionDef:**
- name: archive_cohort_patients
- args: example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients
- body: ['example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 916


#### example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients.0

**Call:**
- func: NotImplementedError
- args: ['example_manifest/cohort.ArrayCohortSystem.archive_cohort_patients.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 917


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write

**FunctionDef:**
- name: assemble_cohort_df_for_write
- args: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write
- body: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write', 'example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 918


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.withColumn
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.1', 'example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 919


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.withColumn
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1.0', 'example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 920


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.agg
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 921


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0

**Call:**
- func: cohort_df.groupBy
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 922


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.0

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.0.0.alias
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 923


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.0.0.0

**Call:**
- func: lit
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 924


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1.0.alias
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 925


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1.0

**Call:**
- func: collect_list
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.0.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 926


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.0.1

**Call:**
- func: lit
- args: ['patient_id_type']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 927


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1.0.cast
- args: ['example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 928


#### example_manifest/cohort.ArrayCohortSystem.assemble_cohort_df_for_write.0.1.0

**Call:**
- func: lit
- args: ['change_dts']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 929


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients

**FunctionDef:**
- name: query_cohort_patients
- args: example_manifest/cohort.ArrayCohortSystem.query_cohort_patients
- body: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients', 'example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.0.0', 'example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0.0']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 930


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.0

**Call:**
- func: example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.0.0.query_cohort_patients
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 931


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.0.0

**Call:**
- func: super
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 932


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1

**Call:**
- func: cohort_df.withColumn
- args: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1', 'example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 933


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0

**Call:**
- func: explode
- args: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 934


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0.0

**Call:**
- func: col
- args: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients.1.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 935


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history

**FunctionDef:**
- name: query_cohort_patients_history
- args: example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history
- body: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 936


#### example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history.0

**Call:**
- func: NotImplementedError
- args: ['example_manifest/cohort.ArrayCohortSystem.query_cohort_patients_history.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 937


#### example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables

**FunctionDef:**
- name: write_empty_cohort_tables
- args: example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables
- body: ['example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 938


#### example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables.0

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.ArrayCohortSystem.write_empty_cohort_tables.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 939


#### example_manifest/cohort.CohortMocker

**ClassDef:**
- name: CohortMocker
- bases: []
- keywords: []
- body: ['example_manifest/cohort.CohortMocker', 'example_manifest/cohort.CohortMocker', 'example_manifest/cohort.CohortMocker.0', 'example_manifest/cohort.CohortMocker.1', 'example_manifest/cohort.CohortMocker.2', 'example_manifest/cohort.CohortMocker.3', 'example_manifest/cohort.CohortMocker.3', 'example_manifest/cohort.CohortMocker.3', 'example_manifest/cohort.CohortMocker.4', 'example_manifest/cohort.CohortMocker.4', 'example_manifest/cohort.CohortMocker.4', 'example_manifest/cohort.CohortMocker.5', 'example_manifest/cohort.CohortMocker.6', 'example_manifest/cohort.CohortMocker.__post_init__', 'example_manifest/cohort.CohortMocker.create_random_cohort', 'example_manifest/cohort.CohortMocker.set_time_observed', 'example_manifest/cohort.CohortMocker.clear_data', 'example_manifest/cohort.CohortMocker.write_mock_data']
- decorator_list: ['dataclass']
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 940


#### example_manifest/cohort.CohortMocker.0

**Call:**
- func: field
- args: []
- keywords: ['example_manifest/cohort.CohortMocker.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 941


#### example_manifest/cohort.CohortMocker.1

**Call:**
- func: int
- args: ['example_manifest/cohort.CohortMocker.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 942


#### example_manifest/cohort.CohortMocker.2

**Call:**
- func: int
- args: ['example_manifest/cohort.CohortMocker.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 943


#### example_manifest/cohort.CohortMocker.3

**Call:**
- func: field
- args: []
- keywords: ['example_manifest/cohort.CohortMocker.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 944


#### example_manifest/cohort.CohortMocker.4

**Call:**
- func: field
- args: []
- keywords: ['example_manifest/cohort.CohortMocker.4']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 945


#### example_manifest/cohort.CohortMocker.5

**Call:**
- func: pd.Timedelta
- args: ['example_manifest/cohort.CohortMocker.5', 'example_manifest/cohort.CohortMocker.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 946


#### example_manifest/cohort.CohortMocker.6

**Call:**
- func: pd.Timedelta
- args: ['example_manifest/cohort.CohortMocker.6', 'example_manifest/cohort.CohortMocker.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 947


#### example_manifest/cohort.CohortMocker.7

**Call:**
- func: pd.Timedelta
- args: ['example_manifest/cohort.CohortMocker.7', 'example_manifest/cohort.CohortMocker.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 948


#### example_manifest/cohort.CohortMocker.__post_init__

**FunctionDef:**
- name: __post_init__
- args: example_manifest/cohort.CohortMocker.__post_init__
- body: ['example_manifest/cohort.CohortMocker.__post_init__', 'example_manifest/cohort.CohortMocker.__post_init__.0', 'example_manifest/cohort.CohortMocker.__post_init__.0', 'example_manifest/cohort.CohortMocker.__post_init__.0', 'example_manifest/cohort.CohortMocker.__post_init__.2', 'example_manifest/cohort.CohortMocker.__post_init__.3', 'example_manifest/cohort.CohortMocker.__post_init__.4', 'example_manifest/cohort.CohortMocker.__post_init__.5', 'example_manifest/cohort.CohortMocker.__post_init__.6.0.2', 'example_manifest/cohort.CohortMocker.__post_init__.6.0.2', 'example_manifest/cohort.CohortMocker.__post_init__.6.0.2', 'example_manifest/cohort.CohortMocker.__post_init__.6.0.2', 'example_manifest/cohort.CohortMocker.__post_init__.7', 'example_manifest/cohort.CohortMocker.__post_init__.9.0', 'example_manifest/cohort.CohortMocker.__post_init__.10.1.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 949


#### example_manifest/cohort.CohortMocker.__post_init__.0

**Call:**
- func: pd.date_range
- args: ['example_manifest/cohort.CohortMocker.__post_init__.0', 'example_manifest/cohort.CohortMocker.__post_init__.0']
- keywords: ['example_manifest/cohort.CohortMocker.__post_init__.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 950


#### example_manifest/cohort.CohortMocker.__post_init__.1

**Call:**
- func: example_manifest/cohort.CohortMocker.__post_init__.1.0.zfill
- args: ['example_manifest/cohort.CohortMocker.__post_init__.1.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 951


#### example_manifest/cohort.CohortMocker.__post_init__.1.0

**Call:**
- func: str
- args: ['x']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 952


#### example_manifest/cohort.CohortMocker.__post_init__.1.1

**Call:**
- func: len
- args: ['example_manifest/cohort.CohortMocker.__post_init__.1.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 953


#### example_manifest/cohort.CohortMocker.__post_init__.1.1.0

**Call:**
- func: str
- args: ['n']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 954


#### example_manifest/cohort.CohortMocker.__post_init__.10

**Call:**
- func: example_manifest/cohort.CohortMocker.__post_init__.10.0.withColumn
- args: ['example_manifest/cohort.CohortMocker.__post_init__.10.0.0', 'example_manifest/cohort.CohortMocker.__post_init__.10.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 955


#### example_manifest/cohort.CohortMocker.__post_init__.10.0

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/cohort.CohortMocker.__post_init__.10.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 956


#### example_manifest/cohort.CohortMocker.__post_init__.10.0.0

**Call:**
- func: pd.concat
- args: ['changelog_dfs']
- keywords: ['example_manifest/cohort.CohortMocker.__post_init__.10.0.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 957


#### example_manifest/cohort.CohortMocker.__post_init__.10.1

**Call:**
- func: example_manifest/cohort.CohortMocker.__post_init__.10.1.0.cast
- args: ['example_manifest/cohort.CohortMocker.__post_init__.10.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 958


#### example_manifest/cohort.CohortMocker.__post_init__.10.1.0

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortMocker.__post_init__.10.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 959


#### example_manifest/cohort.CohortMocker.__post_init__.11

**Call:**
- func: self.set_time_observed
- args: ['example_manifest/cohort.CohortMocker.__post_init__.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 960


#### example_manifest/cohort.CohortMocker.__post_init__.2

**Call:**
- func: range
- args: ['n']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 961


#### example_manifest/cohort.CohortMocker.__post_init__.3

**Call:**
- func: get_possible_ids
- args: ['self.n_all_cohorts']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 962


#### example_manifest/cohort.CohortMocker.__post_init__.4

**Call:**
- func: get_possible_ids
- args: ['self.n_all_patients']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 963


#### example_manifest/cohort.CohortMocker.__post_init__.5

**Call:**
- func: self.rng.choice
- args: ['self.all_possible_report_ids']
- keywords: ['example_manifest/cohort.CohortMocker.__post_init__.5', 'example_manifest/cohort.CohortMocker.__post_init__.5']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 964


#### example_manifest/cohort.CohortMocker.__post_init__.6

**Call:**
- func: example_manifest/cohort.CohortMocker.__post_init__.6.0.drop_duplicates
- args: []
- keywords: ['example_manifest/cohort.CohortMocker.__post_init__.6.0.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 965


#### example_manifest/cohort.CohortMocker.__post_init__.6.0

**Call:**
- func: pd.DataFrame
- args: ['example_manifest/cohort.CohortMocker.__post_init__.6.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 966


#### example_manifest/cohort.CohortMocker.__post_init__.6.0.0

**Call:**
- func: self.rng.choice
- args: ['self.report_ids', 'self.n_patients']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 967


#### example_manifest/cohort.CohortMocker.__post_init__.6.0.1

**Call:**
- func: self.rng.choice
- args: ['self.all_possible_pat_ids', 'self.n_patients']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 968


#### example_manifest/cohort.CohortMocker.__post_init__.6.0.2

**Call:**
- func: self.rng.choice
- args: ['self.update_datetimes', 'self.n_patients']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 969


#### example_manifest/cohort.CohortMocker.__post_init__.7

**Call:**
- func: base_changelog.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 970


#### example_manifest/cohort.CohortMocker.__post_init__.8

**Call:**
- func: self.rng.integers
- args: ['example_manifest/cohort.CohortMocker.__post_init__.8', 'self.anchor_datetimes.size', 'example_manifest/cohort.CohortMocker.__post_init__.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 971


#### example_manifest/cohort.CohortMocker.__post_init__.8.0

**Call:**
- func: len
- args: ['changelog_i']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 972


#### example_manifest/cohort.CohortMocker.__post_init__.9

**Call:**
- func: changelog_dfs.append
- args: ['example_manifest/cohort.CohortMocker.__post_init__.9.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 973


#### example_manifest/cohort.CohortMocker.__post_init__.9.0

**Call:**
- func: changelog_i.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 974


#### example_manifest/cohort.CohortMocker.clear_data

**FunctionDef:**
- name: clear_data
- args: example_manifest/cohort.CohortMocker.clear_data
- body: ['example_manifest/cohort.CohortMocker.clear_data', 'example_manifest/cohort.CohortMocker.clear_data.0', 'example_manifest/cohort.CohortMocker.clear_data.1']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 975


#### example_manifest/cohort.CohortMocker.clear_data.0

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.CohortMocker.clear_data.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 976


#### example_manifest/cohort.CohortMocker.clear_data.1

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.CohortMocker.clear_data.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 977


#### example_manifest/cohort.CohortMocker.clear_data.2

**Call:**
- func: self.cohort_sys.write_empty_cohort_tables
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 978


#### example_manifest/cohort.CohortMocker.create_random_cohort

**FunctionDef:**
- name: create_random_cohort
- args: example_manifest/cohort.CohortMocker.create_random_cohort
- body: ['example_manifest/cohort.CohortMocker.create_random_cohort', 'example_manifest/cohort.CohortMocker.create_random_cohort', 'example_manifest/cohort.CohortMocker.create_random_cohort.0', 'example_manifest/cohort.CohortMocker.create_random_cohort.1.0', 'example_manifest/cohort.CohortMocker.create_random_cohort.2', 'example_manifest/cohort.CohortMocker.create_random_cohort.4', 'example_manifest/cohort.CohortMocker.create_random_cohort.5', 'example_manifest/cohort.CohortMocker.create_random_cohort.6']
- decorator_list: []
- type_params: []
- docstring: While not used for bulk creation because it's slow and doesn't mock up reinsertion,
this is still useful for some test cases.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 979


#### example_manifest/cohort.CohortMocker.create_random_cohort.0

**Call:**
- func: self.rng.choice
- args: ['self.all_possible_pat_ids']
- keywords: ['example_manifest/cohort.CohortMocker.create_random_cohort.0', 'example_manifest/cohort.CohortMocker.create_random_cohort.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 980


#### example_manifest/cohort.CohortMocker.create_random_cohort.1

**Call:**
- func: np.sort
- args: ['example_manifest/cohort.CohortMocker.create_random_cohort.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 981


#### example_manifest/cohort.CohortMocker.create_random_cohort.1.0

**Call:**
- func: self.rng.choice
- args: ['self.update_datetimes']
- keywords: ['example_manifest/cohort.CohortMocker.create_random_cohort.1.0', 'example_manifest/cohort.CohortMocker.create_random_cohort.1.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 982


#### example_manifest/cohort.CohortMocker.create_random_cohort.2

**Call:**
- func: pd.date_range
- args: ['established_dts', 'halted_dts']
- keywords: ['example_manifest/cohort.CohortMocker.create_random_cohort.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 983


#### example_manifest/cohort.CohortMocker.create_random_cohort.3

**Call:**
- func: self.rng.choice
- args: ['update_dates']
- keywords: ['example_manifest/cohort.CohortMocker.create_random_cohort.3', 'example_manifest/cohort.CohortMocker.create_random_cohort.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 984


#### example_manifest/cohort.CohortMocker.create_random_cohort.4

**Call:**
- func: range
- args: ['cohort_size']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 985


#### example_manifest/cohort.CohortMocker.create_random_cohort.5

**Call:**
- func: np.sort
- args: ['unsorted_dates']
- keywords: ['example_manifest/cohort.CohortMocker.create_random_cohort.5']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 986


#### example_manifest/cohort.CohortMocker.create_random_cohort.6

**Call:**
- func: pd.DataFrame
- args: ['example_manifest/cohort.CohortMocker.create_random_cohort.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 987


#### example_manifest/cohort.CohortMocker.set_time_observed

**FunctionDef:**
- name: set_time_observed
- args: example_manifest/cohort.CohortMocker.set_time_observed
- body: ['example_manifest/cohort.CohortMocker.set_time_observed', 'example_manifest/cohort.CohortMocker.set_time_observed', 'example_manifest/cohort.CohortMocker.set_time_observed.0', 'example_manifest/cohort.CohortMocker.set_time_observed.0', 'example_manifest/cohort.CohortMocker.set_time_observed.1', 'example_manifest/cohort.CohortMocker.set_time_observed.1', 'example_manifest/cohort.CohortMocker.set_time_observed.2', 'example_manifest/cohort.CohortMocker.set_time_observed.5', 'example_manifest/cohort.CohortMocker.set_time_observed.6', 'example_manifest/cohort.CohortMocker.set_time_observed.7', 'example_manifest/cohort.CohortMocker.set_time_observed.8.0.0', 'example_manifest/cohort.CohortMocker.set_time_observed.13', 'example_manifest/cohort.CohortMocker.set_time_observed.14', 'example_manifest/cohort.CohortMocker.set_time_observed.15', 'example_manifest/cohort.CohortMocker.set_time_observed.17', 'example_manifest/cohort.CohortMocker.set_time_observed.18.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 988


#### example_manifest/cohort.CohortMocker.set_time_observed.0

**Call:**
- func: np.max
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 989


#### example_manifest/cohort.CohortMocker.set_time_observed.1

**Call:**
- func: np.max
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 990


#### example_manifest/cohort.CohortMocker.set_time_observed.10

**Call:**
- func: self.cohort_sys.utils_sys.query_history_dataframe
- args: ['self.omni_cohort_patients_history']
- keywords: ['example_manifest/cohort.CohortMocker.set_time_observed.10', 'example_manifest/cohort.CohortMocker.set_time_observed.10']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 991


#### example_manifest/cohort.CohortMocker.set_time_observed.11

**Call:**
- func: state_in_history.filter
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 992


#### example_manifest/cohort.CohortMocker.set_time_observed.12

**Call:**
- func: state_in_history.withColumn
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.12', 'example_manifest/cohort.CohortMocker.set_time_observed.12.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 993


#### example_manifest/cohort.CohortMocker.set_time_observed.12.0

**Call:**
- func: example_manifest/cohort.CohortMocker.set_time_observed.12.0.0.cast
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.12.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 994


#### example_manifest/cohort.CohortMocker.set_time_observed.12.0.0

**Call:**
- func: lit
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.12.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 995


#### example_manifest/cohort.CohortMocker.set_time_observed.13

**Call:**
- func: state_in_history.union
- args: ['cohort_patients']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 996


#### example_manifest/cohort.CohortMocker.set_time_observed.14

**Call:**
- func: cohort_patients.select
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.14']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 997


#### example_manifest/cohort.CohortMocker.set_time_observed.15

**Call:**
- func: self.cohort_sys.utils_sys.create_matching_dataframe
- args: ['cohort_patients', 'self.cohort_sys.cohort_patients_df.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 998


#### example_manifest/cohort.CohortMocker.set_time_observed.16

**Call:**
- func: pd.isna
- args: ['self.time_last_archive']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 999


#### example_manifest/cohort.CohortMocker.set_time_observed.17

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.17', 'self.cohort_sys.cohort_patients_history_df.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1000


#### example_manifest/cohort.CohortMocker.set_time_observed.18

**Call:**
- func: self.omni_cohort_patients_history.filter
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.18']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1001


#### example_manifest/cohort.CohortMocker.set_time_observed.18.0

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.18.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1002


#### example_manifest/cohort.CohortMocker.set_time_observed.19

**Call:**
- func: self.cohort_sys.utils_sys.create_matching_dataframe
- args: ['cohort_patients_history', 'self.cohort_sys.cohort_patients_history_df.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1003


#### example_manifest/cohort.CohortMocker.set_time_observed.2

**Call:**
- func: self.cohort_sys.write_empty_cohort_tables
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1004


#### example_manifest/cohort.CohortMocker.set_time_observed.3

**Call:**
- func: pd.isna
- args: ['self.time_last_update']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1005


#### example_manifest/cohort.CohortMocker.set_time_observed.4

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.4', 'self.cohort_sys.cohort_patients_df.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1006


#### example_manifest/cohort.CohortMocker.set_time_observed.5

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.5', 'self.cohort_sys.cohort_patients_history_df.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1007


#### example_manifest/cohort.CohortMocker.set_time_observed.6

**Call:**
- func: self.cohort_sys.utils_sys.query_history_dataframe
- args: ['self.omni_cohort_patients_history']
- keywords: ['example_manifest/cohort.CohortMocker.set_time_observed.6', 'example_manifest/cohort.CohortMocker.set_time_observed.6']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1008


#### example_manifest/cohort.CohortMocker.set_time_observed.7

**Call:**
- func: cohort_patients.filter
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1009


#### example_manifest/cohort.CohortMocker.set_time_observed.8

**Call:**
- func: cohort_patients.withColumn
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.8', 'example_manifest/cohort.CohortMocker.set_time_observed.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1010


#### example_manifest/cohort.CohortMocker.set_time_observed.8.0

**Call:**
- func: example_manifest/cohort.CohortMocker.set_time_observed.8.0.0.cast
- args: ['example_manifest/cohort.CohortMocker.set_time_observed.8.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1011


#### example_manifest/cohort.CohortMocker.set_time_observed.8.0.0

**Call:**
- func: lit
- args: ['self.time_last_update']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1012


#### example_manifest/cohort.CohortMocker.set_time_observed.9

**Call:**
- func: pd.isna
- args: ['self.time_last_archive']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1013


#### example_manifest/cohort.CohortMocker.write_mock_data

**FunctionDef:**
- name: write_mock_data
- args: example_manifest/cohort.CohortMocker.write_mock_data
- body: ['example_manifest/cohort.CohortMocker.write_mock_data', 'example_manifest/cohort.CohortMocker.write_mock_data.0', 'example_manifest/cohort.CohortMocker.write_mock_data.1']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1014


#### example_manifest/cohort.CohortMocker.write_mock_data.0

**Call:**
- func: self.clear_data
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1015


#### example_manifest/cohort.CohortMocker.write_mock_data.1

**Call:**
- func: self.cohort_sys.append_to_table
- args: ['self.cohort_patients_df', 'self.cohort_sys.cohort_patients_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1016


#### example_manifest/cohort.CohortMocker.write_mock_data.2

**Call:**
- func: self.cohort_sys.append_to_table
- args: ['self.cohort_patients_history_df', 'self.cohort_sys.cohort_patients_history_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1017


#### example_manifest/cohort.CohortSystem

**ClassDef:**
- name: CohortSystem
- bases: []
- keywords: []
- body: ['example_manifest/cohort.CohortSystem', 'example_manifest/cohort.CohortSystem.__init__', 'example_manifest/cohort.CohortSystem.cohort_patients_df', 'example_manifest/cohort.CohortSystem.cohort_patients_history_df', 'example_manifest/cohort.CohortSystem.load_cohort', 'example_manifest/cohort.CohortSystem.query_cohort_patients', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history', 'example_manifest/cohort.CohortSystem.write_empty_cohort_tables', 'example_manifest/cohort.CohortSystem.append_to_table', 'example_manifest/cohort.CohortSystem.get_donotcontact_list', 'example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list', 'example_manifest/cohort.CohortSystem.validate_input_cohort', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write', 'example_manifest/cohort.CohortSystem.write_cohort', 'example_manifest/cohort.CohortSystem.update_cohort_patients_history', 'example_manifest/cohort.CohortSystem.clean_cohort_patients']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1018


#### example_manifest/cohort.CohortSystem.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/cohort.CohortSystem.__init__
- body: ['example_manifest/cohort.CohortSystem.__init__', 'example_manifest/cohort.CohortSystem.__init__', 'example_manifest/cohort.CohortSystem.__init__.0', 'example_manifest/cohort.CohortSystem.__init__.1', 'example_manifest/cohort.CohortSystem.__init__.2', 'example_manifest/cohort.CohortSystem.__init__.3', 'example_manifest/cohort.CohortSystem.__init__.4', 'example_manifest/cohort.CohortSystem.__init__.5']
- decorator_list: []
- type_params: []
- docstring: TODO: After the code is in place, review names for consistent naming.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1019


#### example_manifest/cohort.CohortSystem.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1020


#### example_manifest/cohort.CohortSystem.__init__.1

**Call:**
- func: EnvironmentSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1021


#### example_manifest/cohort.CohortSystem.__init__.2

**Call:**
- func: UtilsSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1022


#### example_manifest/cohort.CohortSystem.__init__.3

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/cohort.CohortSystem.__init__.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1023


#### example_manifest/cohort.CohortSystem.__init__.4

**Call:**
- func: self.environment_sys.get_used_path
- args: ['cohort_patients_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1024


#### example_manifest/cohort.CohortSystem.__init__.5

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/cohort.CohortSystem.__init__.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1025


#### example_manifest/cohort.CohortSystem.__init__.6

**Call:**
- func: self.environment_sys.get_used_path
- args: ['cohort_patients_history_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1026


#### example_manifest/cohort.CohortSystem.append_to_table

**FunctionDef:**
- name: append_to_table
- args: example_manifest/cohort.CohortSystem.append_to_table
- body: ['example_manifest/cohort.CohortSystem.append_to_table', 'example_manifest/cohort.CohortSystem.append_to_table', 'example_manifest/cohort.CohortSystem.append_to_table.0.0']
- decorator_list: []
- type_params: []
- docstring: While there's an option to generate an ID column with spark, we opt not to do that
because we want to insure consistency between the main and history tables when writing them.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1027


#### example_manifest/cohort.CohortSystem.append_to_table.0

**Call:**
- func: self.utils_sys.create_matching_dataframe
- args: ['df', 'example_manifest/cohort.CohortSystem.append_to_table.0.0.schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1028


#### example_manifest/cohort.CohortSystem.append_to_table.0.0

**Call:**
- func: self.spark.table
- args: ['path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1029


#### example_manifest/cohort.CohortSystem.append_to_table.1

**Call:**
- func: example_manifest/cohort.CohortSystem.append_to_table.1.0.saveAsTable
- args: ['path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1030


#### example_manifest/cohort.CohortSystem.append_to_table.1.0

**Call:**
- func: df_spark.write.mode
- args: ['example_manifest/cohort.CohortSystem.append_to_table.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1031


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write

**FunctionDef:**
- name: assemble_cohort_df_for_write
- args: example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write
- body: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.1']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1032


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0

**Call:**
- func: example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.withColumn
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1.0', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1033


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0

**Call:**
- func: example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.withColumn
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.1', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1034


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0

**Call:**
- func: example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0.withColumn
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0.0', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1035


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0

**Call:**
- func: cohort_df.withColumn
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0', 'example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1036


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.0.0

**Call:**
- func: lit
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1037


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.0.1

**Call:**
- func: lit
- args: ['patient_id_type']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1038


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1

**Call:**
- func: example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1.0.cast
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1039


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.0.1.0

**Call:**
- func: lit
- args: ['change_dts']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1040


#### example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.1

**Call:**
- func: lit
- args: ['example_manifest/cohort.CohortSystem.assemble_cohort_df_for_write.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1041


#### example_manifest/cohort.CohortSystem.clean_cohort_patients

**FunctionDef:**
- name: clean_cohort_patients
- args: example_manifest/cohort.CohortSystem.clean_cohort_patients
- body: ['example_manifest/cohort.CohortSystem.clean_cohort_patients', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1.0', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.1', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1.0', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.3.0', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.4.0']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1042


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1043


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.0.join
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1']
- keywords: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1.0', 'example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1044


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.0

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.0.0.distinct
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1045


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.0.0

**Call:**
- func: self.cohort_patients_df.select
- args: ['self.id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1046


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1.0.distinct
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1047


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.0.0.1.0

**Call:**
- func: self.cohort_patients_history_df.select
- args: ['self.id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1048


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.1

**Call:**
- func: AssertionError
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1049


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.2

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.2.0.agg
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1050


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.2.0

**Call:**
- func: self.cohort_patients_df.groupBy
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1051


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1.0.alias
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1052


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1.0

**Call:**
- func: max
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.2.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1053


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.3

**Call:**
- func: example_manifest/cohort.CohortSystem.clean_cohort_patients.3.0.filter
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1054


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.3.0

**Call:**
- func: self.cohort_patients_df.join
- args: ['most_recent_df']
- keywords: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.3.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1055


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.4

**Call:**
- func: updated_cohort_patients_df.select
- args: ['example_manifest/cohort.CohortSystem.clean_cohort_patients.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1056


#### example_manifest/cohort.CohortSystem.clean_cohort_patients.4.0

**Call:**
- func: self.cohort_patients_df.schema.fieldNames
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1057


#### example_manifest/cohort.CohortSystem.cohort_patients_df

**FunctionDef:**
- name: cohort_patients_df
- args: example_manifest/cohort.CohortSystem.cohort_patients_df
- body: ['example_manifest/cohort.CohortSystem.cohort_patients_df', 'example_manifest/cohort.CohortSystem.cohort_patients_df']
- decorator_list: ['property']
- type_params: []
- docstring: We make the cohort patients dataframe easily accessible,
but also always pointing to the catalog location.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1058


#### example_manifest/cohort.CohortSystem.cohort_patients_df.0

**Call:**
- func: self.spark.table
- args: ['self.cohort_patients_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1059


#### example_manifest/cohort.CohortSystem.cohort_patients_history_df

**FunctionDef:**
- name: cohort_patients_history_df
- args: example_manifest/cohort.CohortSystem.cohort_patients_history_df
- body: ['example_manifest/cohort.CohortSystem.cohort_patients_history_df', 'example_manifest/cohort.CohortSystem.cohort_patients_history_df']
- decorator_list: ['property']
- type_params: []
- docstring: We make the cohort patients history dataframe easily accessible,
but also always pointing to the catalog location.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1060


#### example_manifest/cohort.CohortSystem.cohort_patients_history_df.0

**Call:**
- func: self.spark.table
- args: ['self.cohort_patients_history_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1061


#### example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list

**FunctionDef:**
- name: filter_cohort_on_donotcontact_list
- args: example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list
- body: ['example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list', 'example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list', 'example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.0', 'example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.1']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: df format: one column, which is pat_id (clarity patient ID).

TODO: Apply filter *only* for recruitment.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1062


#### example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.0

**Call:**
- func: self.get_donotcontact_list
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1063


#### example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.1

**Call:**
- func: df.join
- args: ['donotcontact']
- keywords: ['example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.1', 'example_manifest/cohort.CohortSystem.filter_cohort_on_donotcontact_list.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1064


#### example_manifest/cohort.CohortSystem.get_donotcontact_list

**FunctionDef:**
- name: get_donotcontact_list
- args: example_manifest/cohort.CohortSystem.get_donotcontact_list
- body: ['example_manifest/cohort.CohortSystem.get_donotcontact_list', 'example_manifest/cohort.CohortSystem.get_donotcontact_list.0']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1065


#### example_manifest/cohort.CohortSystem.get_donotcontact_list.0

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.CohortSystem.get_donotcontact_list.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1066


#### example_manifest/cohort.CohortSystem.load_cohort

**FunctionDef:**
- name: load_cohort
- args: example_manifest/cohort.CohortSystem.load_cohort
- body: ['example_manifest/cohort.CohortSystem.load_cohort', 'example_manifest/cohort.CohortSystem.load_cohort.0', 'example_manifest/cohort.CohortSystem.load_cohort.1.0', 'example_manifest/cohort.CohortSystem.load_cohort.3', 'example_manifest/cohort.CohortSystem.load_cohort.4', 'example_manifest/cohort.CohortSystem.load_cohort.5.0', 'example_manifest/cohort.CohortSystem.load_cohort.6.1', 'example_manifest/cohort.CohortSystem.load_cohort.8']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1067


#### example_manifest/cohort.CohortSystem.load_cohort.0

**Call:**
- func: self.query_cohort_patients
- args: ['report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1068


#### example_manifest/cohort.CohortSystem.load_cohort.1

**Call:**
- func: example_manifest/cohort.CohortSystem.load_cohort.1.0.distinct
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1069


#### example_manifest/cohort.CohortSystem.load_cohort.1.0

**Call:**
- func: cohort_df.select
- args: ['example_manifest/cohort.CohortSystem.load_cohort.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1070


#### example_manifest/cohort.CohortSystem.load_cohort.2

**Call:**
- func: patient_id_types.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1071


#### example_manifest/cohort.CohortSystem.load_cohort.3

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.load_cohort.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1072


#### example_manifest/cohort.CohortSystem.load_cohort.4

**Call:**
- func: patient_id_types.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1073


#### example_manifest/cohort.CohortSystem.load_cohort.5

**Call:**
- func: print
- args: ['example_manifest/cohort.CohortSystem.load_cohort.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1074


#### example_manifest/cohort.CohortSystem.load_cohort.5.0

**Call:**
- func: cohort_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1075


#### example_manifest/cohort.CohortSystem.load_cohort.6

**Call:**
- func: example_manifest/cohort.CohortSystem.load_cohort.6.0.withColumnRenamed
- args: ['example_manifest/cohort.CohortSystem.load_cohort.6.0', 'example_manifest/cohort.CohortSystem.load_cohort.6.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1076


#### example_manifest/cohort.CohortSystem.load_cohort.6.0

**Call:**
- func: cohort_df.select
- args: ['example_manifest/cohort.CohortSystem.load_cohort.6.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1077


#### example_manifest/cohort.CohortSystem.load_cohort.6.1

**Call:**
- func: patient_id_type.split
- args: ['example_manifest/cohort.CohortSystem.load_cohort.6.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1078


#### example_manifest/cohort.CohortSystem.load_cohort.7

**Call:**
- func: cohort_df.createOrReplaceTempView
- args: ['view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1079


#### example_manifest/cohort.CohortSystem.load_cohort.8

**Call:**
- func: print
- args: ['example_manifest/cohort.CohortSystem.load_cohort.8']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1080


#### example_manifest/cohort.CohortSystem.query_cohort_patients

**FunctionDef:**
- name: query_cohort_patients
- args: example_manifest/cohort.CohortSystem.query_cohort_patients
- body: ['example_manifest/cohort.CohortSystem.query_cohort_patients', 'example_manifest/cohort.CohortSystem.query_cohort_patients.0.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients.1', 'example_manifest/cohort.CohortSystem.query_cohort_patients.2.0.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients.3', 'example_manifest/cohort.CohortSystem.query_cohort_patients.4']
- decorator_list: []
- returns: DataFrame
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1081


#### example_manifest/cohort.CohortSystem.query_cohort_patients.0

**Call:**
- func: self.cohort_patients_df.filter
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1082


#### example_manifest/cohort.CohortSystem.query_cohort_patients.0.0

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1083


#### example_manifest/cohort.CohortSystem.query_cohort_patients.1

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1084


#### example_manifest/cohort.CohortSystem.query_cohort_patients.2

**Call:**
- func: example_manifest/cohort.CohortSystem.query_cohort_patients.2.0.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1085


#### example_manifest/cohort.CohortSystem.query_cohort_patients.2.0

**Call:**
- func: cohort_df.select
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients.2.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1086


#### example_manifest/cohort.CohortSystem.query_cohort_patients.2.0.0

**Call:**
- func: max
- args: ['update_dts_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1087


#### example_manifest/cohort.CohortSystem.query_cohort_patients.3

**Call:**
- func: cohort_df.filter
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1088


#### example_manifest/cohort.CohortSystem.query_cohort_patients.4

**Call:**
- func: most_recent_cohort_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1089


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history

**FunctionDef:**
- name: query_cohort_patients_history
- args: example_manifest/cohort.CohortSystem.query_cohort_patients_history
- body: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history.1.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history.2.0']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: _summary_

Parameters
----------
report_id : str, optional
    Report to query patients for, defaulting to self.report_id.
time_observed : str | pd.Timestamp, optional
    Point of time at which to check the contents of the cohort,
    defaulting to now.
drop_deleted : bool, optional
    Only return patients actively in the cohort at the specified time,
    by default True

Returns
-------
DataFrame
    _description_

Metadata
--------
- status: in production
- satisfies: can_identify_patients_in_a_given_cohort_at_a_given_time

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**link:**
- source: example_manifest/cohort.CohortSystem.query_cohort_patients_history
- target: can_identify_patients_in_a_given_cohort_at_a_given_time
- link_type: satisfies

**node:**
- connected_component_group: 8

**satisfies**

**status**


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history.0

**Call:**
- func: self.utils_sys.query_history_dataframe
- args: []
- keywords: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history.0', 'example_manifest/cohort.CohortSystem.query_cohort_patients_history.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1090


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history.1

**Call:**
- func: cohort_patients_df_at_time.filter
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1091


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history.1.0

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1092


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history.2

**Call:**
- func: cohort_patients_df_at_time.filter
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1093


#### example_manifest/cohort.CohortSystem.query_cohort_patients_history.2.0

**Call:**
- func: col
- args: ['example_manifest/cohort.CohortSystem.query_cohort_patients_history.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1094


#### example_manifest/cohort.CohortSystem.update_cohort_patients_history

**FunctionDef:**
- name: update_cohort_patients_history
- args: example_manifest/cohort.CohortSystem.update_cohort_patients_history
- body: ['example_manifest/cohort.CohortSystem.update_cohort_patients_history', 'example_manifest/cohort.CohortSystem.update_cohort_patients_history.0']
- decorator_list: []
- returns: example_manifest/cohort.CohortSystem.update_cohort_patients_history.0
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1095


#### example_manifest/cohort.CohortSystem.update_cohort_patients_history.0

**Call:**
- func: self.utils_sys.get_history_updates
- args: ['self.cohort_patients_history_df', 'self.cohort_patients_df']
- keywords: ['example_manifest/cohort.CohortSystem.update_cohort_patients_history.0', 'example_manifest/cohort.CohortSystem.update_cohort_patients_history.0', 'example_manifest/cohort.CohortSystem.update_cohort_patients_history.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1096


#### example_manifest/cohort.CohortSystem.validate_input_cohort

**FunctionDef:**
- name: validate_input_cohort
- args: example_manifest/cohort.CohortSystem.validate_input_cohort
- body: ['example_manifest/cohort.CohortSystem.validate_input_cohort', 'example_manifest/cohort.CohortSystem.validate_input_cohort.2', 'example_manifest/cohort.CohortSystem.validate_input_cohort.4', 'example_manifest/cohort.CohortSystem.validate_input_cohort.6', 'example_manifest/cohort.CohortSystem.validate_input_cohort.8', 'example_manifest/cohort.CohortSystem.validate_input_cohort.8', 'example_manifest/cohort.CohortSystem.validate_input_cohort.8', 'example_manifest/cohort.CohortSystem.validate_input_cohort.9', 'example_manifest/cohort.CohortSystem.validate_input_cohort.10', 'example_manifest/cohort.CohortSystem.validate_input_cohort.11.0.0', 'example_manifest/cohort.CohortSystem.validate_input_cohort.13', 'example_manifest/cohort.CohortSystem.validate_input_cohort.15']
- decorator_list: []
- returns: example_manifest/cohort.CohortSystem.validate_input_cohort.15
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1097


#### example_manifest/cohort.CohortSystem.validate_input_cohort.0

**Call:**
- func: self.spark.catalog.tableExists
- args: ['view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1098


#### example_manifest/cohort.CohortSystem.validate_input_cohort.1

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1099


#### example_manifest/cohort.CohortSystem.validate_input_cohort.10

**Call:**
- func: cohort_df.withColumnRenamed
- args: ['cohort_df_column_name', 'example_manifest/cohort.CohortSystem.validate_input_cohort.10']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1100


#### example_manifest/cohort.CohortSystem.validate_input_cohort.11

**Call:**
- func: example_manifest/cohort.CohortSystem.validate_input_cohort.11.0.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1101


#### example_manifest/cohort.CohortSystem.validate_input_cohort.11.0

**Call:**
- func: example_manifest/cohort.CohortSystem.validate_input_cohort.11.0.0.distinct
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1102


#### example_manifest/cohort.CohortSystem.validate_input_cohort.11.0.0

**Call:**
- func: cohort_df.select
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.11.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1103


#### example_manifest/cohort.CohortSystem.validate_input_cohort.12

**Call:**
- func: cohort_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1104


#### example_manifest/cohort.CohortSystem.validate_input_cohort.13

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.13']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1105


#### example_manifest/cohort.CohortSystem.validate_input_cohort.14

**Call:**
- func: isinstance
- args: ['change_dts', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1106


#### example_manifest/cohort.CohortSystem.validate_input_cohort.15

**Call:**
- func: pd.to_datetime
- args: ['change_dts']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1107


#### example_manifest/cohort.CohortSystem.validate_input_cohort.2

**Call:**
- func: self.spark.table
- args: ['view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1108


#### example_manifest/cohort.CohortSystem.validate_input_cohort.3

**Call:**
- func: isinstance
- args: ['cohort_df', 'example_manifest/cohort.CohortSystem.validate_input_cohort.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1109


#### example_manifest/cohort.CohortSystem.validate_input_cohort.4

**Call:**
- func: TypeError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1110


#### example_manifest/cohort.CohortSystem.validate_input_cohort.5

**Call:**
- func: len
- args: ['cohort_df.columns']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1111


#### example_manifest/cohort.CohortSystem.validate_input_cohort.6

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1112


#### example_manifest/cohort.CohortSystem.validate_input_cohort.7

**Call:**
- func: cohort_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1113


#### example_manifest/cohort.CohortSystem.validate_input_cohort.8

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.8']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1114


#### example_manifest/cohort.CohortSystem.validate_input_cohort.9

**Call:**
- func: ValueError
- args: ['example_manifest/cohort.CohortSystem.validate_input_cohort.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1115


#### example_manifest/cohort.CohortSystem.write_cohort

**FunctionDef:**
- name: write_cohort
- args: example_manifest/cohort.CohortSystem.write_cohort
- body: ['example_manifest/cohort.CohortSystem.write_cohort', 'example_manifest/cohort.CohortSystem.write_cohort', 'example_manifest/cohort.CohortSystem.write_cohort.0', 'example_manifest/cohort.CohortSystem.write_cohort.1', 'example_manifest/cohort.CohortSystem.write_cohort.2', 'example_manifest/cohort.CohortSystem.write_cohort.3']
- decorator_list: []
- type_params: []
- docstring: Note: Before writing we filter on the do-not-contact list.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1116


#### example_manifest/cohort.CohortSystem.write_cohort.0

**Call:**
- func: self.validate_input_cohort
- args: []
- keywords: ['example_manifest/cohort.CohortSystem.write_cohort.0', 'example_manifest/cohort.CohortSystem.write_cohort.0', 'example_manifest/cohort.CohortSystem.write_cohort.0', 'example_manifest/cohort.CohortSystem.write_cohort.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1117


#### example_manifest/cohort.CohortSystem.write_cohort.1

**Call:**
- func: self.filter_cohort_on_donotcontact_list
- args: ['cohort_df']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1118


#### example_manifest/cohort.CohortSystem.write_cohort.2

**Call:**
- func: self.assemble_cohort_df_for_write
- args: []
- keywords: ['example_manifest/cohort.CohortSystem.write_cohort.2', 'example_manifest/cohort.CohortSystem.write_cohort.2', 'example_manifest/cohort.CohortSystem.write_cohort.2', 'example_manifest/cohort.CohortSystem.write_cohort.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1119


#### example_manifest/cohort.CohortSystem.write_cohort.3

**Call:**
- func: self.write_empty_cohort_tables
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1120


#### example_manifest/cohort.CohortSystem.write_cohort.4

**Call:**
- func: self.append_to_table
- args: ['cohort_df', 'self.cohort_patients_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1121


#### example_manifest/cohort.CohortSystem.write_empty_cohort_tables

**FunctionDef:**
- name: write_empty_cohort_tables
- args: example_manifest/cohort.CohortSystem.write_empty_cohort_tables
- body: ['example_manifest/cohort.CohortSystem.write_empty_cohort_tables', 'example_manifest/cohort.CohortSystem.write_empty_cohort_tables.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1122


#### example_manifest/cohort.CohortSystem.write_empty_cohort_tables.0

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.CohortSystem.write_empty_cohort_tables.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1123


#### example_manifest/cohort.CohortSystem.write_empty_cohort_tables.1

**Call:**
- func: self.spark.sql
- args: ['example_manifest/cohort.CohortSystem.write_empty_cohort_tables.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/cohort.py

**node:**
- connected_component_group: 1124


#### example_manifest/data/notebook_templates/cohort

**Module:**
- body: ['example_manifest/data/notebook_templates/cohort.0', 'example_manifest/data/notebook_templates/cohort.0', 'example_manifest/data/notebook_templates/cohort.1', 'example_manifest/data/notebook_templates/cohort.2.0', 'example_manifest/data/notebook_templates/cohort.3', 'example_manifest/data/notebook_templates/cohort.4.0']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1125


#### example_manifest/data/notebook_templates/cohort.0

**ImportFrom:**
- module: ra_lib
- names: [{'name': 'assistant', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1126


#### example_manifest/data/notebook_templates/cohort.1

**Call:**
- func: assistant.ResearchAssistant
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1127


#### example_manifest/data/notebook_templates/cohort.2

**Call:**
- func: display
- args: ['example_manifest/data/notebook_templates/cohort.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1128


#### example_manifest/data/notebook_templates/cohort.2.0

**Call:**
- func: spark.sql
- args: ['example_manifest/data/notebook_templates/cohort.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1129


#### example_manifest/data/notebook_templates/cohort.3

**Call:**
- func: ra.query
- args: ['example_manifest/data/notebook_templates/cohort.3']
- keywords: ['example_manifest/data/notebook_templates/cohort.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1130


#### example_manifest/data/notebook_templates/cohort.4

**Call:**
- func: display
- args: ['example_manifest/data/notebook_templates/cohort.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1131


#### example_manifest/data/notebook_templates/cohort.4.0

**Call:**
- func: spark.table
- args: ['example_manifest/data/notebook_templates/cohort.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1132


#### example_manifest/data/notebook_templates/cohort.5

**Call:**
- func: ra.save_cohort
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/cohort.py

**node:**
- connected_component_group: 1133


#### example_manifest/data/notebook_templates/report

**Module:**
- body: ['example_manifest/data/notebook_templates/report.0', 'example_manifest/data/notebook_templates/report.0', 'example_manifest/data/notebook_templates/report.1', 'example_manifest/data/notebook_templates/report.2', 'example_manifest/data/notebook_templates/report.3', 'example_manifest/data/notebook_templates/report.4.0', 'example_manifest/data/notebook_templates/report.5', 'example_manifest/data/notebook_templates/report.6', 'example_manifest/data/notebook_templates/report.7', 'example_manifest/data/notebook_templates/report.8.0', 'example_manifest/data/notebook_templates/report.9']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1134


#### example_manifest/data/notebook_templates/report.0

**ImportFrom:**
- module: ra_lib
- names: [{'name': 'assistant', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1135


#### example_manifest/data/notebook_templates/report.1

**Call:**
- func: assistant.ResearchAssistant
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1136


#### example_manifest/data/notebook_templates/report.10

**Call:**
- func: ra.save_report_table
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1137


#### example_manifest/data/notebook_templates/report.2

**Call:**
- func: ra.load_cohort
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1138


#### example_manifest/data/notebook_templates/report.3

**Call:**
- func: ra.query
- args: ['example_manifest/data/notebook_templates/report.3']
- keywords: ['example_manifest/data/notebook_templates/report.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1139


#### example_manifest/data/notebook_templates/report.4

**Call:**
- func: display
- args: ['example_manifest/data/notebook_templates/report.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1140


#### example_manifest/data/notebook_templates/report.4.0

**Call:**
- func: spark.table
- args: ['example_manifest/data/notebook_templates/report.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1141


#### example_manifest/data/notebook_templates/report.5

**Call:**
- func: ra.get_connection
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1142


#### example_manifest/data/notebook_templates/report.6

**Call:**
- func: ra.query
- args: ['example_manifest/data/notebook_templates/report.6']
- keywords: ['example_manifest/data/notebook_templates/report.6']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1143


#### example_manifest/data/notebook_templates/report.7

**Call:**
- func: ra.query
- args: ['example_manifest/data/notebook_templates/report.7']
- keywords: ['example_manifest/data/notebook_templates/report.7', 'example_manifest/data/notebook_templates/report.7']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1144


#### example_manifest/data/notebook_templates/report.8

**Call:**
- func: display
- args: ['example_manifest/data/notebook_templates/report.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1145


#### example_manifest/data/notebook_templates/report.8.0

**Call:**
- func: spark.table
- args: ['example_manifest/data/notebook_templates/report.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1146


#### example_manifest/data/notebook_templates/report.9

**Call:**
- func: connection.close
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/notebook_templates/report.py

**node:**
- connected_component_group: 1147


#### example_manifest/data/regex/transform_regex

**Module:**
- body: ['example_manifest/data/regex/transform_regex.0', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.1', 'example_manifest/data/regex/transform_regex.2.0.0', 'example_manifest/data/regex/transform_regex.2.0.0', 'example_manifest/data/regex/transform_regex.2.0.0', 'example_manifest/data/regex/transform_regex.2.0.0', 'example_manifest/data/regex/transform_regex.3.0.0', 'example_manifest/data/regex/transform_regex.3.0.0', 'example_manifest/data/regex/transform_regex.3.0.0', 'example_manifest/data/regex/transform_regex.3.0.0', 'example_manifest/data/regex/transform_regex.4.0.0', 'example_manifest/data/regex/transform_regex.4.0.0', 'example_manifest/data/regex/transform_regex.4.0.0', 'example_manifest/data/regex/transform_regex.4.0.0', 'example_manifest/data/regex/transform_regex.4.0.0']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1148


#### example_manifest/data/regex/transform_regex.0

**Import:**
- names: [{'name': 'os', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1149


#### example_manifest/data/regex/transform_regex.1

**Import:**
- names: [{'name': 'json', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1150


#### example_manifest/data/regex/transform_regex.10

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'staging_terms']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1151


#### example_manifest/data/regex/transform_regex.10.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'gene_symbols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1152


#### example_manifest/data/regex/transform_regex.10.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'town_names']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1153


#### example_manifest/data/regex/transform_regex.10.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'ones']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1154


#### example_manifest/data/regex/transform_regex.10.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'decades_lt_90']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1155


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'teens']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1156


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'holidays']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1157


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'full_numbering']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1158


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'state_names']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1159


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'address_indicator']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1160


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'seasons']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1161


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'day_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1162


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0

**Call:**
- func: example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'day_numbering']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1163


#### example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0

**Call:**
- func: regex.replace
- args: ['example_manifest/data/regex/transform_regex.10.0.0.0.0.0.0.0.0.0.0.0.0.0', 'month_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1164


#### example_manifest/data/regex/transform_regex.11

**Call:**
- func: open
- args: ['new_filepath', 'example_manifest/data/regex/transform_regex.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1165


#### example_manifest/data/regex/transform_regex.12

**Call:**
- func: fin.write
- args: ['regex']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1166


#### example_manifest/data/regex/transform_regex.2

**Call:**
- func: json.loads
- args: ['example_manifest/data/regex/transform_regex.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1167


#### example_manifest/data/regex/transform_regex.2.0

**Call:**
- func: example_manifest/data/regex/transform_regex.2.0.0.read
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1168


#### example_manifest/data/regex/transform_regex.2.0.0

**Call:**
- func: open
- args: ['example_manifest/data/regex/transform_regex.2.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1169


#### example_manifest/data/regex/transform_regex.3

**Call:**
- func: json.loads
- args: ['example_manifest/data/regex/transform_regex.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1170


#### example_manifest/data/regex/transform_regex.3.0

**Call:**
- func: example_manifest/data/regex/transform_regex.3.0.0.read
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1171


#### example_manifest/data/regex/transform_regex.3.0.0

**Call:**
- func: open
- args: ['example_manifest/data/regex/transform_regex.3.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1172


#### example_manifest/data/regex/transform_regex.4

**Call:**
- func: json.loads
- args: ['example_manifest/data/regex/transform_regex.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1173


#### example_manifest/data/regex/transform_regex.4.0

**Call:**
- func: example_manifest/data/regex/transform_regex.4.0.0.read
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1174


#### example_manifest/data/regex/transform_regex.4.0.0

**Call:**
- func: open
- args: ['example_manifest/data/regex/transform_regex.4.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1175


#### example_manifest/data/regex/transform_regex.5

**Call:**
- func: os.walk
- args: ['rootdir']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1176


#### example_manifest/data/regex/transform_regex.6

**Call:**
- func: os.path.join
- args: ['subdir', 'file']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1177


#### example_manifest/data/regex/transform_regex.7

**Call:**
- func: file.split
- args: ['example_manifest/data/regex/transform_regex.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1178


#### example_manifest/data/regex/transform_regex.8

**Call:**
- func: os.path.join
- args: ['subdir', 'new_file_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1179


#### example_manifest/data/regex/transform_regex.9

**Call:**
- func: example_manifest/data/regex/transform_regex.9.0.strip
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1180


#### example_manifest/data/regex/transform_regex.9.0

**Call:**
- func: example_manifest/data/regex/transform_regex.9.0.0.read
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1181


#### example_manifest/data/regex/transform_regex.9.0.0

**Call:**
- func: open
- args: ['filepath', 'example_manifest/data/regex/transform_regex.9.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/data/regex/transform_regex.py

**node:**
- connected_component_group: 1182


#### example_manifest/environment

**Module:**
- body: ['example_manifest/environment.0', 'example_manifest/environment.1', 'example_manifest/environment.2', 'example_manifest/environment.3', 'example_manifest/environment.4', 'example_manifest/environment.5', 'example_manifest/environment.6', 'example_manifest/environment.7', 'example_manifest/environment.EnvironmentSystem', 'example_manifest/environment.EnvironmentSystem.get_secret.2', 'example_manifest/environment.EnvironmentSystem.get_secret.2', 'example_manifest/environment.EnvironmentSystem.get_secret.2']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1183


#### example_manifest/environment.0

**Import:**
- names: [{'name': 'os', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1184


#### example_manifest/environment.1

**Import:**
- names: [{'name': 're', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1185


#### example_manifest/environment.2

**Import:**
- names: [{'name': 'warnings', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1186


#### example_manifest/environment.3

**Import:**
- names: [{'name': 'IPython', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1187


#### example_manifest/environment.4

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1188


#### example_manifest/environment.5

**ImportFrom:**
- module: pyspark.errors
- names: [{'name': 'PySparkException', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1189


#### example_manifest/environment.6

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1190


#### example_manifest/environment.7

**ImportFrom:**
- module: pyspark.sql.functions
- names: [{'name': 'lit', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1191


#### example_manifest/environment.EnvironmentSystem

**ClassDef:**
- name: EnvironmentSystem
- bases: []
- keywords: []
- body: ['example_manifest/environment.EnvironmentSystem', 'example_manifest/environment.EnvironmentSystem', 'example_manifest/environment.EnvironmentSystem', 'example_manifest/environment.EnvironmentSystem.__init__', 'example_manifest/environment.EnvironmentSystem.get', 'example_manifest/environment.EnvironmentSystem.set', 'example_manifest/environment.EnvironmentSystem.chdir_to_nbdir', 'example_manifest/environment.EnvironmentSystem.remove_test_tables', 'example_manifest/environment.EnvironmentSystem.warn', 'example_manifest/environment.EnvironmentSystem.get_used_path', 'example_manifest/environment.EnvironmentSystem.get_context', 'example_manifest/environment.EnvironmentSystem.get_workspace', 'example_manifest/environment.EnvironmentSystem.get_user_category', 'example_manifest/environment.EnvironmentSystem.get_user_dir', 'example_manifest/environment.EnvironmentSystem.get_username', 'example_manifest/environment.EnvironmentSystem.get_params_view_name', 'example_manifest/environment.EnvironmentSystem.get_report_id', 'example_manifest/environment.EnvironmentSystem.get_used_for_report', 'example_manifest/environment.EnvironmentSystem.get_notebook_dirname', 'example_manifest/environment.EnvironmentSystem.get_notebook_path', 'example_manifest/environment.EnvironmentSystem.get_notebook_context', 'example_manifest/environment.EnvironmentSystem.get_secret']
- decorator_list: []
- type_params: []
- docstring: Note to developers: we might be able to separate out the get logic into a separate system,
which we can then use to get values from arbitrary classes.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1192


#### example_manifest/environment.EnvironmentSystem.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/environment.EnvironmentSystem.__init__
- body: ['example_manifest/environment.EnvironmentSystem.__init__', 'example_manifest/environment.EnvironmentSystem.__init__', 'example_manifest/environment.EnvironmentSystem.__init__.0', 'example_manifest/environment.EnvironmentSystem.__init__.1', 'example_manifest/environment.EnvironmentSystem.__init__.2', 'example_manifest/environment.EnvironmentSystem.__init__.3', 'example_manifest/environment.EnvironmentSystem.__init__.4', 'example_manifest/environment.EnvironmentSystem.__init__.4', 'example_manifest/environment.EnvironmentSystem.__init__.7', 'example_manifest/environment.EnvironmentSystem.__init__.9', 'example_manifest/environment.EnvironmentSystem.__init__.10']
- decorator_list: []
- type_params: []
- docstring: Throughout we refer to a "parameters view".

TODO: Currently everything has a "report_id", even when ra_lib is not being used for a report.
We probably want to use some sort of "ra_lib instance id" instead. But less wordy.

TODO: Currently the parameters view is only used for ensuring our tests are using test mode.
It's not clear this is worth the added complexity. Evaluate.

Parameters
----------
report_id : str
    This ID is defined even when we're not

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1193


#### example_manifest/environment.EnvironmentSystem.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1194


#### example_manifest/environment.EnvironmentSystem.__init__.1

**Call:**
- func: IPython.get_ipython
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1195


#### example_manifest/environment.EnvironmentSystem.__init__.10

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.__init__.10']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1196


#### example_manifest/environment.EnvironmentSystem.__init__.11

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.__init__.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1197


#### example_manifest/environment.EnvironmentSystem.__init__.2

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.__init__.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1198


#### example_manifest/environment.EnvironmentSystem.__init__.3

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.__init__.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1199


#### example_manifest/environment.EnvironmentSystem.__init__.4

**Call:**
- func: self.spark.conf.get
- args: ['example_manifest/environment.EnvironmentSystem.__init__.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1200


#### example_manifest/environment.EnvironmentSystem.__init__.5

**Call:**
- func: self.spark.catalog.tableExists
- args: ['self.params_view_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1201


#### example_manifest/environment.EnvironmentSystem.__init__.6

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/environment.EnvironmentSystem.__init__.6']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1202


#### example_manifest/environment.EnvironmentSystem.__init__.7

**Call:**
- func: params_df.createOrReplaceGlobalTempView
- args: ['self.params_view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1203


#### example_manifest/environment.EnvironmentSystem.__init__.8

**Call:**
- func: provided_params.items
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1204


#### example_manifest/environment.EnvironmentSystem.__init__.9

**Call:**
- func: self.set
- args: ['key', 'value']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1205


#### example_manifest/environment.EnvironmentSystem.chdir_to_nbdir

**FunctionDef:**
- name: chdir_to_nbdir
- args: example_manifest/environment.EnvironmentSystem.chdir_to_nbdir
- body: ['example_manifest/environment.EnvironmentSystem.chdir_to_nbdir', 'example_manifest/environment.EnvironmentSystem.chdir_to_nbdir']
- decorator_list: []
- type_params: []
- docstring: When run inside a notebook, this changes the working directory to that of the notebook.
This is the default for Databricks 14+, and is therefore not necessary in those environments.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1206


#### example_manifest/environment.EnvironmentSystem.chdir_to_nbdir.0

**Call:**
- func: os.chdir
- args: ['example_manifest/environment.EnvironmentSystem.chdir_to_nbdir.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1207


#### example_manifest/environment.EnvironmentSystem.chdir_to_nbdir.0.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.chdir_to_nbdir.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1208


#### example_manifest/environment.EnvironmentSystem.get

**FunctionDef:**
- name: get
- args: example_manifest/environment.EnvironmentSystem.get
- body: ['example_manifest/environment.EnvironmentSystem.get', 'example_manifest/environment.EnvironmentSystem.get.2', 'example_manifest/environment.EnvironmentSystem.get.4', 'example_manifest/environment.EnvironmentSystem.get.6.0', 'example_manifest/environment.EnvironmentSystem.get.11', 'example_manifest/environment.EnvironmentSystem.get.12']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1209


#### example_manifest/environment.EnvironmentSystem.get.0

**Call:**
- func: hasattr
- args: ['self', 'example_manifest/environment.EnvironmentSystem.get.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1210


#### example_manifest/environment.EnvironmentSystem.get.1

**Call:**
- func: getattr
- args: ['self', 'example_manifest/environment.EnvironmentSystem.get.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1211


#### example_manifest/environment.EnvironmentSystem.get.10

**Call:**
- func: isinstance
- args: ['contexts_value', 'dict']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1212


#### example_manifest/environment.EnvironmentSystem.get.11

**Call:**
- func: contexts_value.get
- args: ['self.context', 'example_manifest/environment.EnvironmentSystem.get.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1213


#### example_manifest/environment.EnvironmentSystem.get.12

**Call:**
- func: self.warn
- args: ['example_manifest/environment.EnvironmentSystem.get.12']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1214


#### example_manifest/environment.EnvironmentSystem.get.2

**Call:**
- func: getter_method
- args: ['example_manifest/environment.EnvironmentSystem.get.2']
- keywords: ['example_manifest/environment.EnvironmentSystem.get.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1215


#### example_manifest/environment.EnvironmentSystem.get.3

**Call:**
- func: hasattr
- args: ['self', 'example_manifest/environment.EnvironmentSystem.get.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1216


#### example_manifest/environment.EnvironmentSystem.get.4

**Call:**
- func: self.spark.catalog.tableExists
- args: ['self.params_view_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1217


#### example_manifest/environment.EnvironmentSystem.get.5

**Call:**
- func: self.spark.table
- args: ['self.params_view_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1218


#### example_manifest/environment.EnvironmentSystem.get.6

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get.6.0.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1219


#### example_manifest/environment.EnvironmentSystem.get.6.0

**Call:**
- func: params.select
- args: ['key']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1220


#### example_manifest/environment.EnvironmentSystem.get.7

**Call:**
- func: len
- args: ['args']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1221


#### example_manifest/environment.EnvironmentSystem.get.8

**Call:**
- func: len
- args: ['kwargs']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1222


#### example_manifest/environment.EnvironmentSystem.get.9

**Call:**
- func: ValueError
- args: ['example_manifest/environment.EnvironmentSystem.get.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1223


#### example_manifest/environment.EnvironmentSystem.get_context

**FunctionDef:**
- name: get_context
- args: example_manifest/environment.EnvironmentSystem.get_context
- body: ['example_manifest/environment.EnvironmentSystem.get_context']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1224


#### example_manifest/environment.EnvironmentSystem.get_context.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_context.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1225


#### example_manifest/environment.EnvironmentSystem.get_context.1

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_context.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1226


#### example_manifest/environment.EnvironmentSystem.get_notebook_context

**FunctionDef:**
- name: get_notebook_context
- args: example_manifest/environment.EnvironmentSystem.get_notebook_context
- body: ['example_manifest/environment.EnvironmentSystem.get_notebook_context']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1227


#### example_manifest/environment.EnvironmentSystem.get_notebook_context.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_notebook_context.0.0.getContext
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1228


#### example_manifest/environment.EnvironmentSystem.get_notebook_context.0.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_notebook_context.0.0.0.notebook
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1229


#### example_manifest/environment.EnvironmentSystem.get_notebook_context.0.0.0

**Call:**
- func: self.dbutils.notebook.entry_point.getDbutils
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1230


#### example_manifest/environment.EnvironmentSystem.get_notebook_dirname

**FunctionDef:**
- name: get_notebook_dirname
- args: example_manifest/environment.EnvironmentSystem.get_notebook_dirname
- body: ['example_manifest/environment.EnvironmentSystem.get_notebook_dirname', 'example_manifest/environment.EnvironmentSystem.get_notebook_dirname', 'example_manifest/environment.EnvironmentSystem.get_notebook_dirname.0', 'example_manifest/environment.EnvironmentSystem.get_notebook_dirname.1']
- decorator_list: []
- returns: str
- type_params: []
- docstring: Get the name of the notebook directory itself, without any other path information.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1231


#### example_manifest/environment.EnvironmentSystem.get_notebook_dirname.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_notebook_dirname.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1232


#### example_manifest/environment.EnvironmentSystem.get_notebook_dirname.1

**Call:**
- func: os.path.dirname
- args: ['notebook_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1233


#### example_manifest/environment.EnvironmentSystem.get_notebook_dirname.2

**Call:**
- func: os.path.basename
- args: ['notebook_dir']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1234


#### example_manifest/environment.EnvironmentSystem.get_notebook_path

**FunctionDef:**
- name: get_notebook_path
- args: example_manifest/environment.EnvironmentSystem.get_notebook_path
- body: ['example_manifest/environment.EnvironmentSystem.get_notebook_path', 'example_manifest/environment.EnvironmentSystem.get_notebook_path']
- decorator_list: []
- returns: str
- type_params: []
- docstring: When run inside a notebook, this returns the path of the notebook.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1235


#### example_manifest/environment.EnvironmentSystem.get_notebook_path.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_notebook_path.0.0.get
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1236


#### example_manifest/environment.EnvironmentSystem.get_notebook_path.0.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_notebook_path.0.0.0.notebookPath
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1237


#### example_manifest/environment.EnvironmentSystem.get_notebook_path.0.0.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_notebook_path.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1238


#### example_manifest/environment.EnvironmentSystem.get_params_view_name

**FunctionDef:**
- name: get_params_view_name
- args: example_manifest/environment.EnvironmentSystem.get_params_view_name
- body: ['example_manifest/environment.EnvironmentSystem.get_params_view_name', 'example_manifest/environment.EnvironmentSystem.get_params_view_name.0', 'example_manifest/environment.EnvironmentSystem.get_params_view_name.1']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1239


#### example_manifest/environment.EnvironmentSystem.get_params_view_name.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_params_view_name.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1240


#### example_manifest/environment.EnvironmentSystem.get_params_view_name.1

**Call:**
- func: re.sub
- args: ['example_manifest/environment.EnvironmentSystem.get_params_view_name.1', 'example_manifest/environment.EnvironmentSystem.get_params_view_name.1', 'report_id']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1241


#### example_manifest/environment.EnvironmentSystem.get_report_id

**FunctionDef:**
- name: get_report_id
- args: example_manifest/environment.EnvironmentSystem.get_report_id
- body: ['example_manifest/environment.EnvironmentSystem.get_report_id', 'example_manifest/environment.EnvironmentSystem.get_report_id', 'example_manifest/environment.EnvironmentSystem.get_report_id.0', 'example_manifest/environment.EnvironmentSystem.get_report_id.1', 'example_manifest/environment.EnvironmentSystem.get_report_id.5.0.0']
- decorator_list: []
- returns: str
- type_params: []
- docstring: Parse the notebook path to get identifying information.
Only having the ID in the notebook directory path prevents having mismatched IDs.

Returns
-------
report_id : str
    The id of the report, as listed in `research_dm.research_cohort.config`. This is typically the id of the AzDO ticket.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1242


#### example_manifest/environment.EnvironmentSystem.get_report_id.0

**Call:**
- func: hasattr
- args: ['self', 'example_manifest/environment.EnvironmentSystem.get_report_id.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1243


#### example_manifest/environment.EnvironmentSystem.get_report_id.1

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_report_id.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1244


#### example_manifest/environment.EnvironmentSystem.get_report_id.2

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_report_id.2']
- keywords: ['example_manifest/environment.EnvironmentSystem.get_report_id.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1245


#### example_manifest/environment.EnvironmentSystem.get_report_id.3

**Call:**
- func: os.path.dirname
- args: ['path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1246


#### example_manifest/environment.EnvironmentSystem.get_report_id.4

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_report_id.4.0.split
- args: ['example_manifest/environment.EnvironmentSystem.get_report_id.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1247


#### example_manifest/environment.EnvironmentSystem.get_report_id.4.0

**Call:**
- func: os.path.basename
- args: ['dir_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1248


#### example_manifest/environment.EnvironmentSystem.get_report_id.5

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_report_id.5.0.split
- args: ['example_manifest/environment.EnvironmentSystem.get_report_id.5.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1249


#### example_manifest/environment.EnvironmentSystem.get_report_id.5.0

**Call:**
- func: os.path.basename
- args: ['example_manifest/environment.EnvironmentSystem.get_report_id.5.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1250


#### example_manifest/environment.EnvironmentSystem.get_report_id.5.0.0

**Call:**
- func: os.path.dirname
- args: ['dir_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1251


#### example_manifest/environment.EnvironmentSystem.get_secret

**FunctionDef:**
- name: get_secret
- args: example_manifest/environment.EnvironmentSystem.get_secret
- body: ['example_manifest/environment.EnvironmentSystem.get_secret', 'example_manifest/environment.EnvironmentSystem.get_secret.0', 'example_manifest/environment.EnvironmentSystem.get_secret.1']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1252


#### example_manifest/environment.EnvironmentSystem.get_secret.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_secret.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1253


#### example_manifest/environment.EnvironmentSystem.get_secret.1

**Call:**
- func: self.get
- args: ['secret_key']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1254


#### example_manifest/environment.EnvironmentSystem.get_secret.2

**Call:**
- func: self.dbutils.secrets.get
- args: ['scope', 'secret_key']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1255


#### example_manifest/environment.EnvironmentSystem.get_used_for_report

**FunctionDef:**
- name: get_used_for_report
- args: example_manifest/environment.EnvironmentSystem.get_used_for_report
- body: ['example_manifest/environment.EnvironmentSystem.get_used_for_report', 'example_manifest/environment.EnvironmentSystem.get_used_for_report.0']
- decorator_list: []
- returns: bool
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1256


#### example_manifest/environment.EnvironmentSystem.get_used_for_report.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_used_for_report.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1257


#### example_manifest/environment.EnvironmentSystem.get_used_path

**FunctionDef:**
- name: get_used_path
- args: example_manifest/environment.EnvironmentSystem.get_used_path
- body: ['example_manifest/environment.EnvironmentSystem.get_used_path', 'example_manifest/environment.EnvironmentSystem.get_used_path', 'example_manifest/environment.EnvironmentSystem.get_used_path.0', 'example_manifest/environment.EnvironmentSystem.get_used_path.1', 'example_manifest/environment.EnvironmentSystem.get_used_path.3', 'example_manifest/environment.EnvironmentSystem.get_used_path.5', 'example_manifest/environment.EnvironmentSystem.get_used_path.6', 'example_manifest/environment.EnvironmentSystem.get_used_path.8']
- decorator_list: []
- returns: str
- type_params: []
- docstring: Wrapping table paths in this function ensures that when in dev
the table is piped to a location we can write to. We also prepend the table
name with a label when in test mode.

Parameters
----------
path : str
    The path to the table in dev or stg.
dev_schema : str, optional
    The schema the table should be at in dev, by
    default "sandbox.scratch_research"

Returns
-------
str
    The table path, given the environment.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1258


#### example_manifest/environment.EnvironmentSystem.get_used_path.0

**Call:**
- func: path.split
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1259


#### example_manifest/environment.EnvironmentSystem.get_used_path.1

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1260


#### example_manifest/environment.EnvironmentSystem.get_used_path.2

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_used_path.2.join
- args: ['split_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1261


#### example_manifest/environment.EnvironmentSystem.get_used_path.3

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_used_path.3.join
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.3']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1262


#### example_manifest/environment.EnvironmentSystem.get_used_path.4

**Call:**
- func: len
- args: ['split_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1263


#### example_manifest/environment.EnvironmentSystem.get_used_path.5

**Call:**
- func: schema.split
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1264


#### example_manifest/environment.EnvironmentSystem.get_used_path.6

**Call:**
- func: len
- args: ['split_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1265


#### example_manifest/environment.EnvironmentSystem.get_used_path.7

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1266


#### example_manifest/environment.EnvironmentSystem.get_used_path.8

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_used_path.8']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1267


#### example_manifest/environment.EnvironmentSystem.get_user_category

**FunctionDef:**
- name: get_user_category
- args: example_manifest/environment.EnvironmentSystem.get_user_category
- body: ['example_manifest/environment.EnvironmentSystem.get_user_category']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1268


#### example_manifest/environment.EnvironmentSystem.get_user_category.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_user_category.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1269


#### example_manifest/environment.EnvironmentSystem.get_user_dir

**FunctionDef:**
- name: get_user_dir
- args: example_manifest/environment.EnvironmentSystem.get_user_dir
- body: ['example_manifest/environment.EnvironmentSystem.get_user_dir']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1270


#### example_manifest/environment.EnvironmentSystem.get_user_dir.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_user_dir.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1271


#### example_manifest/environment.EnvironmentSystem.get_username

**FunctionDef:**
- name: get_username
- args: example_manifest/environment.EnvironmentSystem.get_username
- body: ['example_manifest/environment.EnvironmentSystem.get_username']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1272


#### example_manifest/environment.EnvironmentSystem.get_username.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_username.0.0.get
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1273


#### example_manifest/environment.EnvironmentSystem.get_username.0.0

**Call:**
- func: example_manifest/environment.EnvironmentSystem.get_username.0.0.0.userName
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1274


#### example_manifest/environment.EnvironmentSystem.get_username.0.0.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.get_username.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1275


#### example_manifest/environment.EnvironmentSystem.get_workspace

**FunctionDef:**
- name: get_workspace
- args: example_manifest/environment.EnvironmentSystem.get_workspace
- body: ['example_manifest/environment.EnvironmentSystem.get_workspace']
- decorator_list: []
- returns: str
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1276


#### example_manifest/environment.EnvironmentSystem.get_workspace.0

**Call:**
- func: self.spark.conf.get
- args: ['example_manifest/environment.EnvironmentSystem.get_workspace.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1277


#### example_manifest/environment.EnvironmentSystem.remove_test_tables

**FunctionDef:**
- name: remove_test_tables
- args: example_manifest/environment.EnvironmentSystem.remove_test_tables
- body: ['example_manifest/environment.EnvironmentSystem.remove_test_tables', 'example_manifest/environment.EnvironmentSystem.remove_test_tables.0', 'example_manifest/environment.EnvironmentSystem.remove_test_tables.1.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1278


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.0

**Call:**
- func: isinstance
- args: ['schemas', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1279


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.1

**Call:**
- func: pd.unique
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1280


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.1.0

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.1.0', 'schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1281


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.10

**Call:**
- func: example_manifest/environment.EnvironmentSystem.remove_test_tables.10.0.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1282


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.10.0

**Call:**
- func: tables_df.select
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.10.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1283


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.11

**Call:**
- func: self.spark.sql
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.11']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1284


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.12

**Call:**
- func: print
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.12']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1285


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.13

**Call:**
- func: ex.getErrorClass
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1286


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.14

**Call:**
- func: print
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.14']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1287


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.14.0

**Call:**
- func: ex.getErrorClass
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1288


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.2

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1289


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.3

**Call:**
- func: self.get
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.3', 'schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1290


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.4

**Call:**
- func: print
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1291


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.5

**Call:**
- func: self.spark.sql
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.5']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1292


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.6

**Call:**
- func: ex.getErrorClass
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1293


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.7

**Call:**
- func: print
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1294


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.8

**Call:**
- func: tables_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1295


#### example_manifest/environment.EnvironmentSystem.remove_test_tables.9

**Call:**
- func: print
- args: ['example_manifest/environment.EnvironmentSystem.remove_test_tables.9']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1296


#### example_manifest/environment.EnvironmentSystem.set

**FunctionDef:**
- name: set
- args: example_manifest/environment.EnvironmentSystem.set
- body: ['example_manifest/environment.EnvironmentSystem.set', 'example_manifest/environment.EnvironmentSystem.set.0', 'example_manifest/environment.EnvironmentSystem.set.1', 'example_manifest/environment.EnvironmentSystem.set.2', 'example_manifest/environment.EnvironmentSystem.set.3']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1297


#### example_manifest/environment.EnvironmentSystem.set.0

**Call:**
- func: ValueError
- args: ['example_manifest/environment.EnvironmentSystem.set.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1298


#### example_manifest/environment.EnvironmentSystem.set.1

**Call:**
- func: lit
- args: ['value']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1299


#### example_manifest/environment.EnvironmentSystem.set.2

**Call:**
- func: self.spark.table
- args: ['self.params_view_path']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1300


#### example_manifest/environment.EnvironmentSystem.set.3

**Call:**
- func: params_df.withColumn
- args: ['key', 'spark_value']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1301


#### example_manifest/environment.EnvironmentSystem.set.4

**Call:**
- func: params_df.createOrReplaceGlobalTempView
- args: ['self.params_view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1302


#### example_manifest/environment.EnvironmentSystem.warn

**FunctionDef:**
- name: warn
- args: example_manifest/environment.EnvironmentSystem.warn
- body: ['example_manifest/environment.EnvironmentSystem.warn', 'example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning', 'example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning', 'example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning']
- decorator_list: ['property']
- type_params: []
- docstring: The default warnings.warn function is noisy. While this isn't a major deal,
we really do want to minimize the amount of possibly confusing text.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1303


#### example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning

**FunctionDef:**
- name: custom_formatwarning
- args: example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning
- body: ['example_manifest/environment.EnvironmentSystem.warn.custom_formatwarning']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/environment.py

**node:**
- connected_component_group: 1304


#### example_manifest/query

**Module:**
- body: ['example_manifest/query.0', 'example_manifest/query.1', 'example_manifest/query.2', 'example_manifest/query.3', 'example_manifest/query.4', 'example_manifest/query.5', 'example_manifest/query.6', 'example_manifest/query.7', 'example_manifest/query.OnPremQuerySystem', 'example_manifest/query.Connection', 'example_manifest/query.PyMSSQLConnection']
- type_ignores: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1305


#### example_manifest/query.0

**Import:**
- names: [{'name': 'json', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1306


#### example_manifest/query.1

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1307


#### example_manifest/query.2

**Import:**
- names: [{'name': 'pymssql', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1308


#### example_manifest/query.3

**ImportFrom:**
- module: pyspark.sql.dataframe
- names: [{'name': 'DataFrame', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1309


#### example_manifest/query.4

**ImportFrom:**
- module: pyspark.sql.connect.dataframe
- names: [{'name': 'DataFrame', 'asname': 'ConnectDataFrame'}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1310


#### example_manifest/query.5

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1311


#### example_manifest/query.6

**Import:**
- names: [{'name': 'sqlalchemy', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1312


#### example_manifest/query.7

**ImportFrom:**
- module: environment
- names: [{'name': 'EnvironmentSystem', 'asname': None}]
- level: 1

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1313


#### example_manifest/query.Connection

**ClassDef:**
- name: Connection
- bases: []
- keywords: []
- body: ['example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.establish_connection']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1314


#### example_manifest/query.Connection.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/query.Connection.__init__
- body: ['example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.__init__', 'example_manifest/query.Connection.__init__']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1315


#### example_manifest/query.Connection.__init__.0

**Call:**
- func: self.establish_connection
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1316


#### example_manifest/query.Connection.establish_connection

**FunctionDef:**
- name: establish_connection
- args: example_manifest/query.Connection.establish_connection
- body: ['example_manifest/query.Connection.establish_connection', 'example_manifest/query.Connection.establish_connection']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1317


#### example_manifest/query.Connection.establish_connection.0

**Call:**
- func: sqlalchemy.create_engine
- args: ['connection_string']
- keywords: ['example_manifest/query.Connection.establish_connection.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1318


#### example_manifest/query.OnPremQuerySystem

**ClassDef:**
- name: OnPremQuerySystem
- bases: []
- keywords: []
- body: ['example_manifest/query.OnPremQuerySystem', 'example_manifest/query.OnPremQuerySystem.__init__', 'example_manifest/query.OnPremQuerySystem.query', 'example_manifest/query.OnPremQuerySystem.conn', 'example_manifest/query.OnPremQuerySystem.refresh_connection', 'example_manifest/query.OnPremQuerySystem.get_open_connection', 'example_manifest/query.OnPremQuerySystem.query_from_connection', 'example_manifest/query.OnPremQuerySystem.convert_cursor']
- decorator_list: []
- type_params: []
- docstring: Class for querying on-prem data.

Metadata
--------
- satisfies: can_query_onprem_data
- status: in production

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**link:**
- source: example_manifest/query.OnPremQuerySystem
- target: can_query_onprem_data
- link_type: satisfies

**node:**
- connected_component_group: 19

**satisfies**

**status**


#### example_manifest/query.OnPremQuerySystem.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/query.OnPremQuerySystem.__init__
- body: ['example_manifest/query.OnPremQuerySystem.__init__', 'example_manifest/query.OnPremQuerySystem.__init__.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1319


#### example_manifest/query.OnPremQuerySystem.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1320


#### example_manifest/query.OnPremQuerySystem.__init__.1

**Call:**
- func: EnvironmentSystem
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1321


#### example_manifest/query.OnPremQuerySystem.conn

**FunctionDef:**
- name: conn
- args: example_manifest/query.OnPremQuerySystem.conn
- body: ['example_manifest/query.OnPremQuerySystem.conn', 'example_manifest/query.OnPremQuerySystem.conn.4.1']
- decorator_list: ['property']
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1322


#### example_manifest/query.OnPremQuerySystem.conn.0

**Call:**
- func: hasattr
- args: ['self', 'example_manifest/query.OnPremQuerySystem.conn.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1323


#### example_manifest/query.OnPremQuerySystem.conn.1

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/query.OnPremQuerySystem.conn.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1324


#### example_manifest/query.OnPremQuerySystem.conn.2

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/query.OnPremQuerySystem.conn.2', 'example_manifest/query.OnPremQuerySystem.conn.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1325


#### example_manifest/query.OnPremQuerySystem.conn.3

**Call:**
- func: json.loads
- args: ['secret']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1326


#### example_manifest/query.OnPremQuerySystem.conn.4

**Call:**
- func: Connection
- args: []
- keywords: ['example_manifest/query.OnPremQuerySystem.conn.4', 'example_manifest/query.OnPremQuerySystem.conn.4', 'example_manifest/query.OnPremQuerySystem.conn.4.0', 'example_manifest/query.OnPremQuerySystem.conn.4.0', 'example_manifest/query.OnPremQuerySystem.conn.4.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1327


#### example_manifest/query.OnPremQuerySystem.conn.4.0

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/query.OnPremQuerySystem.conn.4.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1328


#### example_manifest/query.OnPremQuerySystem.conn.4.1

**Call:**
- func: self.environment_sys.get
- args: ['example_manifest/query.OnPremQuerySystem.conn.4.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1329


#### example_manifest/query.OnPremQuerySystem.convert_cursor

**FunctionDef:**
- name: convert_cursor
- args: example_manifest/query.OnPremQuerySystem.convert_cursor
- body: ['example_manifest/query.OnPremQuerySystem.convert_cursor', 'example_manifest/query.OnPremQuerySystem.convert_cursor', 'example_manifest/query.OnPremQuerySystem.convert_cursor', 'example_manifest/query.OnPremQuerySystem.convert_cursor.0', 'example_manifest/query.OnPremQuerySystem.convert_cursor.1', 'example_manifest/query.OnPremQuerySystem.convert_cursor.1', 'example_manifest/query.OnPremQuerySystem.convert_cursor.2.0', 'example_manifest/query.OnPremQuerySystem.convert_cursor.2.0', 'example_manifest/query.OnPremQuerySystem.convert_cursor.3', 'example_manifest/query.OnPremQuerySystem.convert_cursor.3', 'example_manifest/query.OnPremQuerySystem.convert_cursor.4']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1330


#### example_manifest/query.OnPremQuerySystem.convert_cursor.0

**Call:**
- func: ValueError
- args: ['example_manifest/query.OnPremQuerySystem.convert_cursor.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1331


#### example_manifest/query.OnPremQuerySystem.convert_cursor.1

**Call:**
- func: print
- args: ['example_manifest/query.OnPremQuerySystem.convert_cursor.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1332


#### example_manifest/query.OnPremQuerySystem.convert_cursor.2

**Call:**
- func: pd.DataFrame
- args: ['example_manifest/query.OnPremQuerySystem.convert_cursor.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1333


#### example_manifest/query.OnPremQuerySystem.convert_cursor.2.0

**Call:**
- func: cursor.fetchall
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1334


#### example_manifest/query.OnPremQuerySystem.convert_cursor.3

**Call:**
- func: self.spark.createDataFrame
- args: ['result_pdf']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1335


#### example_manifest/query.OnPremQuerySystem.convert_cursor.4

**Call:**
- func: result_sdf.createOrReplaceTempView
- args: ['view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1336


#### example_manifest/query.OnPremQuerySystem.get_open_connection

**FunctionDef:**
- name: get_open_connection
- args: example_manifest/query.OnPremQuerySystem.get_open_connection
- body: ['example_manifest/query.OnPremQuerySystem.get_open_connection']
- decorator_list: []
- returns: sqlalchemy.engine.base.Connection
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1337


#### example_manifest/query.OnPremQuerySystem.get_open_connection.0

**Call:**
- func: self.conn.engine.connect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1338


#### example_manifest/query.OnPremQuerySystem.query

**FunctionDef:**
- name: query
- args: example_manifest/query.OnPremQuerySystem.query
- body: ['example_manifest/query.OnPremQuerySystem.query', 'example_manifest/query.OnPremQuerySystem.query', 'example_manifest/query.OnPremQuerySystem.query.1', 'example_manifest/query.OnPremQuerySystem.query.4']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: Main function for querying data.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1339


#### example_manifest/query.OnPremQuerySystem.query.0

**Call:**
- func: list
- args: ['example_manifest/query.OnPremQuerySystem.query.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1340


#### example_manifest/query.OnPremQuerySystem.query.0.0

**Call:**
- func: example_manifest/query.OnPremQuerySystem.query.0.0.0.values.flatten
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1341


#### example_manifest/query.OnPremQuerySystem.query.0.0.0

**Call:**
- func: example_manifest/query.OnPremQuerySystem.query.0.0.0.0.toPandas
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1342


#### example_manifest/query.OnPremQuerySystem.query.0.0.0.0

**Call:**
- func: self.spark.table
- args: ['example_manifest/query.OnPremQuerySystem.query.0.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1343


#### example_manifest/query.OnPremQuerySystem.query.1

**Call:**
- func: execute_kwargs.update
- args: ['example_manifest/query.OnPremQuerySystem.query.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1344


#### example_manifest/query.OnPremQuerySystem.query.2

**Call:**
- func: self.query_from_connection
- args: ['sql_query', 'view_name', 'connection']
- keywords: ['example_manifest/query.OnPremQuerySystem.query.2', 'example_manifest/query.OnPremQuerySystem.query.2']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1345


#### example_manifest/query.OnPremQuerySystem.query.3

**Call:**
- func: self.get_open_connection
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1346


#### example_manifest/query.OnPremQuerySystem.query.4

**Call:**
- func: self.query_from_connection
- args: ['sql_query', 'view_name', 'connection']
- keywords: ['example_manifest/query.OnPremQuerySystem.query.4', 'example_manifest/query.OnPremQuerySystem.query.4']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1347


#### example_manifest/query.OnPremQuerySystem.query_from_connection

**FunctionDef:**
- name: query_from_connection
- args: example_manifest/query.OnPremQuerySystem.query_from_connection
- body: ['example_manifest/query.OnPremQuerySystem.query_from_connection', 'example_manifest/query.OnPremQuerySystem.query_from_connection.0.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1348


#### example_manifest/query.OnPremQuerySystem.query_from_connection.0

**Call:**
- func: connection.execute
- args: ['example_manifest/query.OnPremQuerySystem.query_from_connection.0.0']
- keywords: ['example_manifest/query.OnPremQuerySystem.query_from_connection.0.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1349


#### example_manifest/query.OnPremQuerySystem.query_from_connection.0.0

**Call:**
- func: sqlalchemy.text
- args: ['sql_query']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1350


#### example_manifest/query.OnPremQuerySystem.query_from_connection.1

**Call:**
- func: self.convert_cursor
- args: ['result', 'output_as', 'view_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1351


#### example_manifest/query.OnPremQuerySystem.refresh_connection

**FunctionDef:**
- name: refresh_connection
- args: example_manifest/query.OnPremQuerySystem.refresh_connection
- body: ['example_manifest/query.OnPremQuerySystem.refresh_connection', 'example_manifest/query.OnPremQuerySystem.refresh_connection']
- decorator_list: []
- type_params: []
- docstring: Clears out the _conn attribute so it can be recreated, potentially with updated environment
parameters.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1352


#### example_manifest/query.OnPremQuerySystem.refresh_connection.0

**Call:**
- func: hasattr
- args: ['self', 'example_manifest/query.OnPremQuerySystem.refresh_connection.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1353


#### example_manifest/query.OnPremQuerySystem.refresh_connection.1

**Call:**
- func: hasattr
- args: ['self._conn', 'example_manifest/query.OnPremQuerySystem.refresh_connection.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1354


#### example_manifest/query.OnPremQuerySystem.refresh_connection.2

**Call:**
- func: self._conn.close
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1355


#### example_manifest/query.PyMSSQLConnection

**ClassDef:**
- name: PyMSSQLConnection
- bases: ['Connection']
- keywords: []
- body: ['example_manifest/query.PyMSSQLConnection.establish_connection']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1356


#### example_manifest/query.PyMSSQLConnection.establish_connection

**FunctionDef:**
- name: establish_connection
- args: example_manifest/query.PyMSSQLConnection.establish_connection
- body: ['example_manifest/query.PyMSSQLConnection.establish_connection']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1357


#### example_manifest/query.PyMSSQLConnection.establish_connection.0

**Call:**
- func: pymssql.connect
- args: []
- keywords: ['example_manifest/query.PyMSSQLConnection.establish_connection.0', 'example_manifest/query.PyMSSQLConnection.establish_connection.0', 'example_manifest/query.PyMSSQLConnection.establish_connection.0', 'example_manifest/query.PyMSSQLConnection.establish_connection.0', 'example_manifest/query.PyMSSQLConnection.establish_connection.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/query.py

**node:**
- connected_component_group: 1358


#### example_manifest/utils

**Module:**
- body: ['example_manifest/utils', 'example_manifest/utils.0', 'example_manifest/utils.1', 'example_manifest/utils.2', 'example_manifest/utils.3', 'example_manifest/utils.4', 'example_manifest/utils.5', 'example_manifest/utils.6', 'example_manifest/utils.UtilsSystem', 'example_manifest/utils.get_dataframe_changelog']
- type_ignores: []
- docstring: The utils module contains convenience methods that do not depend on any other code
inside ra_lib. Functions added here should be used in multiple contexts,
or at the very least they should be general purpose.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1359


#### example_manifest/utils.0

**Import:**
- names: [{'name': 're', 'asname': None}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1360


#### example_manifest/utils.1

**Import:**
- names: [{'name': 'pandas', 'asname': 'pd'}]

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1361


#### example_manifest/utils.2

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'SparkSession', 'asname': None}, {'name': 'Window', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1362


#### example_manifest/utils.3

**ImportFrom:**
- module: pyspark.sql
- names: [{'name': 'functions', 'asname': 'sqlfn'}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1363


#### example_manifest/utils.4

**ImportFrom:**
- module: pyspark.sql.dataframe
- names: [{'name': 'DataFrame', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1364


#### example_manifest/utils.5

**ImportFrom:**
- module: pyspark.sql.types
- names: [{'name': 'StructType', 'asname': None}, {'name': 'StructField', 'asname': None}, {'name': 'StringType', 'asname': None}, {'name': 'IntegerType', 'asname': None}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1365


#### example_manifest/utils.6

**ImportFrom:**
- module: pyspark.sql.connect.dataframe
- names: [{'name': 'DataFrame', 'asname': 'ConnectDataFrame'}]
- level: 0

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1366


#### example_manifest/utils.UtilsSystem

**ClassDef:**
- name: UtilsSystem
- bases: []
- keywords: []
- body: ['example_manifest/utils.UtilsSystem', 'example_manifest/utils.UtilsSystem.__init__', 'example_manifest/utils.UtilsSystem.query_history_dataframe', 'example_manifest/utils.UtilsSystem.get_history_updates', 'example_manifest/utils.UtilsSystem.get_history_summary', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog', 'example_manifest/utils.UtilsSystem.get_dataframe_diff', 'example_manifest/utils.UtilsSystem.create_matching_dataframe', 'example_manifest/utils.UtilsSystem.sanitize_dirname']
- decorator_list: []
- type_params: []
- docstring: UtilsSystem is the main class of the utils module.

One of UtilsSystem's main functions is to record table history for auditing purposes.
This involves the use of a selected table ("current_df") and its history ("history_df").
This system operates under a few requirements:
1. current_df contains a series of snapshots of different groups at different times
2. history_df contains the changes in group membership, up to and including the earliest snapshot per group stored in current_df.
If these assumptions are followed then current_df and history_df can be operated in a manner to allow current_df to receive
concurrent updates without conflict. Note that both current_df and history_df must include the full data needed to reproduce
the earliest snapshot per group. This enables us to record both the 

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1367


#### example_manifest/utils.UtilsSystem.__init__

**FunctionDef:**
- name: __init__
- args: example_manifest/utils.UtilsSystem.__init__
- body: ['example_manifest/utils.UtilsSystem.__init__', 'example_manifest/utils.UtilsSystem.__init__', 'example_manifest/utils.UtilsSystem.__init__.0', 'example_manifest/utils.UtilsSystem.__init__.0']
- decorator_list: []
- type_params: []
- docstring: Construct an instance of UtilsSystem.

TODO: Reconcile what should and shouldn't be an attribute. We probably don't want change_type_col and change_time_col
to be parameters because it should be vanishingly rare that we use something other than the defaults.

Parameters
----------
self.change_time_col : str
    Column name for the column that tracks changes in history tables.
self.change_type_col : str
    Column name for the column that tracks change type in history tables.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1368


#### example_manifest/utils.UtilsSystem.__init__.0

**Call:**
- func: SparkSession.builder.getOrCreate
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1369


#### example_manifest/utils.UtilsSystem.create_matching_dataframe

**FunctionDef:**
- name: create_matching_dataframe
- args: example_manifest/utils.UtilsSystem.create_matching_dataframe
- body: ['example_manifest/utils.UtilsSystem.create_matching_dataframe', 'example_manifest/utils.UtilsSystem.create_matching_dataframe', 'example_manifest/utils.UtilsSystem.create_matching_dataframe', 'example_manifest/utils.UtilsSystem.create_matching_dataframe.2']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: PySpark's createDataFrame does not validate column order when creating
spark DataFrames from pandas DataFrames, which can result in schema mismatch.
The same schema mismatch can occur between spark DataFrames. This function
ensures that at least the columns match.

This function does not ensure type matching between spark DataFrames at this
time, but that would be straightforward enough to implement.

Parameters
----------
source_df : pd.DataFrame | DataFrame
    pandas or spark DataFrame to reformat
target_schema : StructType
    spark schema to match

Returns
-------
DataFrame
    source_df reformatted

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1370


#### example_manifest/utils.UtilsSystem.create_matching_dataframe.0

**Call:**
- func: isinstance
- args: ['source_df', 'example_manifest/utils.UtilsSystem.create_matching_dataframe.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1371


#### example_manifest/utils.UtilsSystem.create_matching_dataframe.1

**Call:**
- func: self.spark.createDataFrame
- args: ['df']
- keywords: ['example_manifest/utils.UtilsSystem.create_matching_dataframe.1']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1372


#### example_manifest/utils.UtilsSystem.create_matching_dataframe.2

**Call:**
- func: source_df.select
- args: ['columns']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1373


#### example_manifest/utils.UtilsSystem.get_dataframe_diff

**FunctionDef:**
- name: get_dataframe_diff
- args: example_manifest/utils.UtilsSystem.get_dataframe_diff
- body: ['example_manifest/utils.UtilsSystem.get_dataframe_diff', 'example_manifest/utils.UtilsSystem.get_dataframe_diff', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.1', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.1', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.2', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.3.1.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.5.0.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.7', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.8.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.12.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.13', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.14.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.15', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.16.0', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.17']
- decorator_list: []
- returns: example_manifest/utils.UtilsSystem.get_dataframe_diff.17
- type_params: []
- docstring: Compare a new dataframe with the data in the old dataframe to identify
rows that were inserted or deleted.

The diff only tracks the insertion and deletion of rows, not updates
Regarding tracking exact updates and querying a table at an arbitrary time,
the best option for that is probably to use delta lake table history.
While it's only maintained for 7 days by default, we could export from it to
an archival location. The code in this module can be used to test the solution.

On timestamps:
- The new dataframe can contain data from multiple updates if
    it has a time column, but only the most recent change will be added.
- The timestamp for changes, when not provided, is the time of function call
- If time_col_in_new_df is provided and diff_time is not then we use the
    the latest time in new_df for the diff_time for deleted rows

Assumptions:
- No values in old_df are recorded after any values in new_df or after diff_time
- In order for a row to be tracked as deleted it must exist in the history
    table but not the new dataframe.

Parameters
----------
old_df : DataFrame
    Previous version of the dataframe.
new_df : DataFrame
    Updated version of the dataframe.
id_col : str | list[str]
    One or more columns that uniquely identifies a given row in the table that
    history_df is based on. For example, for cohort_patients this is
    ["report_id", "patient_id", "patient_id_type"].
time_col_in_new_df : str, optional
    If provided this is the column containing the time a change was made in
    new_df.
diff_time : str | pd.Timestamp, optional
    The time at which this operation takes place. Defaults to now.

Returns
-------
DataFrame
    A dataframe containing id_col, a column tracking when a row was inserted
    or deleted ("change_datetime" by default), and a column tracking the type
    of change ("inserted" or "deleted"; "change_type" by default)

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1374


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.0

**Call:**
- func: new_df.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1375


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.1

**Call:**
- func: old_df.select
- args: ['id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1376


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.10

**Call:**
- func: new_df.withColumnRenamed
- args: ['time_col_in_new_df', 'self.change_time_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1377


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.11

**Call:**
- func: dict
- args: ['new_df.dtypes']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1378


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.12

**Call:**
- func: old_df.withColumn
- args: ['self.change_time_col', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.12.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1379


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.12.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_dataframe_diff.12.0.cast
- args: ['new_df_time_dtype']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1380


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.13

**Call:**
- func: new_df.join
- args: ['old_df']
- keywords: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.13', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.13']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1381


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.14

**Call:**
- func: inserted_df.withColumn
- args: ['self.change_type_col', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.14.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1382


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.14.0

**Call:**
- func: sqlfn.lit
- args: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.14.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1383


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.15

**Call:**
- func: old_df.join
- args: ['new_df']
- keywords: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.15', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.15']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1384


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.16

**Call:**
- func: deleted_df.withColumn
- args: ['self.change_type_col', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.16.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1385


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.16.0

**Call:**
- func: sqlfn.lit
- args: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.16.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1386


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.17

**Call:**
- func: inserted_df.union
- args: ['deleted_df']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1387


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.2

**Call:**
- func: new_df.select
- args: ['selected_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1388


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.3

**Call:**
- func: example_manifest/utils.UtilsSystem.get_dataframe_diff.3.0.agg
- args: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.3.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1389


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.3.0

**Call:**
- func: new_df.groupby
- args: ['id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1390


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.3.1

**Call:**
- func: example_manifest/utils.UtilsSystem.get_dataframe_diff.3.1.0.alias
- args: ['time_col_in_new_df']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1391


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.3.1.0

**Call:**
- func: sqlfn.min
- args: ['time_col_in_new_df']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1392


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.4

**Call:**
- func: pd.Timestamp.now
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1393


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.5

**Call:**
- func: example_manifest/utils.UtilsSystem.get_dataframe_diff.5.0.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1394


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.5.0

**Call:**
- func: new_df.select
- args: ['example_manifest/utils.UtilsSystem.get_dataframe_diff.5.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1395


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.5.0.0

**Call:**
- func: sqlfn.max
- args: ['time_col_in_new_df']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1396


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.6

**Call:**
- func: isinstance
- args: ['diff_time', 'str']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1397


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.7

**Call:**
- func: pd.Timestamp
- args: ['diff_time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1398


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.8

**Call:**
- func: old_df.withColumn
- args: ['self.change_time_col', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1399


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.8.0

**Call:**
- func: sqlfn.lit
- args: ['diff_time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1400


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.9

**Call:**
- func: new_df.withColumn
- args: ['self.change_time_col', 'example_manifest/utils.UtilsSystem.get_dataframe_diff.9.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1401


#### example_manifest/utils.UtilsSystem.get_dataframe_diff.9.0

**Call:**
- func: sqlfn.lit
- args: ['diff_time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1402


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog

**FunctionDef:**
- name: get_grouped_dataframe_changelog
- args: example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog
- body: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply.0', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.0', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.3.0', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.4', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.6']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1403


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.0

**Call:**
- func: df.select
- args: ['id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1404


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.1

**Call:**
- func: StructField
- args: ['self.change_type_col', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1405


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.1.0

**Call:**
- func: StringType
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1406


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.2

**Call:**
- func: StructField
- args: ['self.change_time_col', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.2.dataType']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1407


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.2.0

**Call:**
- func: df.select
- args: ['time_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1408


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.3

**Call:**
- func: StructField
- args: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.3', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1409


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.3.0

**Call:**
- func: IntegerType
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1410


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.4

**Call:**
- func: StructType
- args: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1411


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5

**Call:**
- func: self.spark.createDataFrame
- args: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1412


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0.0.apply
- args: ['fn_to_apply']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1413


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0.0.0.groupby
- args: ['group_key']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1414


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.5.0.0.0

**Call:**
- func: df.toPandas
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1415


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.6

**Call:**
- func: self.create_matching_dataframe
- args: ['change_df', 'schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1416


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.7

**Call:**
- func: example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.7.0.applyInPandas
- args: ['fn_to_apply', 'schema']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1417


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.7.0

**Call:**
- func: df.groupBy
- args: ['group_key']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1418


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply

**FunctionDef:**
- name: fn_to_apply
- args: example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply
- body: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1419


#### example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply.0

**Call:**
- func: get_dataframe_changelog
- args: ['df']
- keywords: ['example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply.0', 'example_manifest/utils.UtilsSystem.get_grouped_dataframe_changelog.fn_to_apply.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1420


#### example_manifest/utils.UtilsSystem.get_history_summary

**FunctionDef:**
- name: get_history_summary
- args: example_manifest/utils.UtilsSystem.get_history_summary
- body: ['example_manifest/utils.UtilsSystem.get_history_summary', 'example_manifest/utils.UtilsSystem.get_history_summary.0.0.0']
- decorator_list: []
- type_params: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1421


#### example_manifest/utils.UtilsSystem.get_history_summary.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_history_summary.0.0.collect
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1422


#### example_manifest/utils.UtilsSystem.get_history_summary.0.0

**Call:**
- func: history_df.select
- args: ['example_manifest/utils.UtilsSystem.get_history_summary.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1423


#### example_manifest/utils.UtilsSystem.get_history_summary.0.0.0

**Call:**
- func: sqlfn.min
- args: ['time_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1424


#### example_manifest/utils.UtilsSystem.get_history_summary.1

**Call:**
- func: example_manifest/utils.UtilsSystem.get_history_summary.1.0.orderBy
- args: ['example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1425


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.count
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1426


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.groupby
- args: ['example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1427


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0

**Call:**
- func: example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0.withColumn
- args: ['example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0.0', 'example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1428


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0

**Call:**
- func: history_df.withColumn
- args: ['example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0', 'example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1429


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.0.0

**Call:**
- func: sqlfn.lit
- args: ['t_0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1430


#### example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.1

**Call:**
- func: sqlfn.datediff
- args: ['time_col', 'example_manifest/utils.UtilsSystem.get_history_summary.1.0.0.0.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1431


#### example_manifest/utils.UtilsSystem.get_history_updates

**FunctionDef:**
- name: get_history_updates
- args: example_manifest/utils.UtilsSystem.get_history_updates
- body: ['example_manifest/utils.UtilsSystem.get_history_updates', 'example_manifest/utils.UtilsSystem.get_history_updates', 'example_manifest/utils.UtilsSystem.get_history_updates.0', 'example_manifest/utils.UtilsSystem.get_history_updates.1.0']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: Given a dataframe current_df with changes tracked in a table history_table,
update history_table with a record of the latest changes.

Parameters
----------
history_table_path : str
    Location of the table containing the history
current_df : DataFrame
    DataFrame containing the current version of the table.
id_col : str | list[str]
    One or more columns that uniquely identifies a given row in the table that
    history_df is based on. For example, for cohort_patients this is
    ["report_id", "patient_id", "patient_id_type"].
time_col_in_current_df : str
    Column containing the time a change was made to current_df
time_between_updates : pd.Timedelta, optional
    Allowed time between updates, by default pd.Timedelta(1, "d"). Multiple
    updates closer together than time_between_updates will be counted as
    a single update.

Side Effects
------------
table at history_table_path:
    This table is updated.

Returns
-------
DataFrame
    A dataframe showing the changes made to the history table.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1432


#### example_manifest/utils.UtilsSystem.get_history_updates.0

**Call:**
- func: self.get_grouped_dataframe_changelog
- args: ['current_df']
- keywords: ['example_manifest/utils.UtilsSystem.get_history_updates.0', 'example_manifest/utils.UtilsSystem.get_history_updates.0', 'example_manifest/utils.UtilsSystem.get_history_updates.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1433


#### example_manifest/utils.UtilsSystem.get_history_updates.1

**Call:**
- func: changelog_df.join
- args: ['example_manifest/utils.UtilsSystem.get_history_updates.1.0']
- keywords: ['example_manifest/utils.UtilsSystem.get_history_updates.1.0', 'example_manifest/utils.UtilsSystem.get_history_updates.1.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1434


#### example_manifest/utils.UtilsSystem.get_history_updates.1.0

**Call:**
- func: history_df.select
- args: ['example_manifest/utils.UtilsSystem.get_history_updates.1.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1435


#### example_manifest/utils.UtilsSystem.get_history_updates.2

**Call:**
- func: history_updates_df.select
- args: ['example_manifest/utils.UtilsSystem.get_history_updates.2']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1436


#### example_manifest/utils.UtilsSystem.query_history_dataframe

**FunctionDef:**
- name: query_history_dataframe
- args: example_manifest/utils.UtilsSystem.query_history_dataframe
- body: ['example_manifest/utils.UtilsSystem.query_history_dataframe', 'example_manifest/utils.UtilsSystem.query_history_dataframe', 'example_manifest/utils.UtilsSystem.query_history_dataframe.0.0', 'example_manifest/utils.UtilsSystem.query_history_dataframe.1.1', 'example_manifest/utils.UtilsSystem.query_history_dataframe.2.0.0', 'example_manifest/utils.UtilsSystem.query_history_dataframe.3.0']
- decorator_list: []
- returns: DataFrame
- type_params: []
- docstring: Given a dataframe history_df that records the rows inserted and deleted
from a table "original_table", this method identifies the rows that were
present in original_table at the specified time.

This could be done in spark sql, but we opt to do it using pyspark because
it's easier to parameterize. For example, id_col here can either be a single
column name or a list of column names.

Parameters:
----------
history_df : DataFrame
    A dataframe recording the history of a table. It should consist of at
    least id_col and self.change_time_col.
id_col : str | list[str]
    One or more columns that uniquely identifies a given row in the table that
    history_df is based on. For example, for cohort_patients this is
    ["report_id", "patient_id", "patient_id_type"].
time : str | pd.Timestamp, optional
    The time at which you want to get the rows in original_table. Defaults
    to the current time.

Returns
-------
DataFrame
    The dataframe tracked by history_df at the specified time.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1437


#### example_manifest/utils.UtilsSystem.query_history_dataframe.0

**Call:**
- func: history_df.filter
- args: ['example_manifest/utils.UtilsSystem.query_history_dataframe.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1438


#### example_manifest/utils.UtilsSystem.query_history_dataframe.0.0

**Call:**
- func: sqlfn.col
- args: ['self.change_time_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1439


#### example_manifest/utils.UtilsSystem.query_history_dataframe.1

**Call:**
- func: example_manifest/utils.UtilsSystem.query_history_dataframe.1.0.orderBy
- args: ['example_manifest/utils.UtilsSystem.query_history_dataframe.1.1']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1440


#### example_manifest/utils.UtilsSystem.query_history_dataframe.1.0

**Call:**
- func: Window.partitionBy
- args: ['id_cols']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1441


#### example_manifest/utils.UtilsSystem.query_history_dataframe.1.1

**Call:**
- func: sqlfn.desc
- args: ['self.change_time_col']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1442


#### example_manifest/utils.UtilsSystem.query_history_dataframe.2

**Call:**
- func: history_df.withColumn
- args: ['example_manifest/utils.UtilsSystem.query_history_dataframe.2', 'example_manifest/utils.UtilsSystem.query_history_dataframe.2.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1443


#### example_manifest/utils.UtilsSystem.query_history_dataframe.2.0

**Call:**
- func: example_manifest/utils.UtilsSystem.query_history_dataframe.2.0.0.over
- args: ['w']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1444


#### example_manifest/utils.UtilsSystem.query_history_dataframe.2.0.0

**Call:**
- func: sqlfn.row_number
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1445


#### example_manifest/utils.UtilsSystem.query_history_dataframe.3

**Call:**
- func: example_manifest/utils.UtilsSystem.query_history_dataframe.3.0.drop
- args: ['example_manifest/utils.UtilsSystem.query_history_dataframe.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1446


#### example_manifest/utils.UtilsSystem.query_history_dataframe.3.0

**Call:**
- func: history_df_with_rn.filter
- args: ['example_manifest/utils.UtilsSystem.query_history_dataframe.3.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1447


#### example_manifest/utils.UtilsSystem.sanitize_dirname

**FunctionDef:**
- name: sanitize_dirname
- args: example_manifest/utils.UtilsSystem.sanitize_dirname
- body: ['example_manifest/utils.UtilsSystem.sanitize_dirname', 'example_manifest/utils.UtilsSystem.sanitize_dirname', 'example_manifest/utils.UtilsSystem.sanitize_dirname.0.0', 'example_manifest/utils.UtilsSystem.sanitize_dirname.1', 'example_manifest/utils.UtilsSystem.sanitize_dirname.2']
- decorator_list: []
- returns: str
- type_params: []
- docstring: Sanitizes a directory name by removing invalid characters
and replacing spaces with underscores.

Parameters
----------
name: str
    The original directory name.

Returns
-------
str
    A sanitized directory name.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1448


#### example_manifest/utils.UtilsSystem.sanitize_dirname.0

**Call:**
- func: re.sub
- args: ['example_manifest/utils.UtilsSystem.sanitize_dirname.0', 'space_sub', 'example_manifest/utils.UtilsSystem.sanitize_dirname.0.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1449


#### example_manifest/utils.UtilsSystem.sanitize_dirname.0.0

**Call:**
- func: name.lower
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1450


#### example_manifest/utils.UtilsSystem.sanitize_dirname.1

**Call:**
- func: re.sub
- args: ['example_manifest/utils.UtilsSystem.sanitize_dirname.1', 'example_manifest/utils.UtilsSystem.sanitize_dirname.1', 'sanitized_name']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1451


#### example_manifest/utils.UtilsSystem.sanitize_dirname.2

**Call:**
- func: sanitized_name.strip
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1452


#### example_manifest/utils.get_dataframe_changelog

**FunctionDef:**
- name: get_dataframe_changelog
- args: example_manifest/utils.get_dataframe_changelog
- body: ['example_manifest/utils.get_dataframe_changelog', 'example_manifest/utils.get_dataframe_changelog', 'example_manifest/utils.get_dataframe_changelog', 'example_manifest/utils.get_dataframe_changelog.0', 'example_manifest/utils.get_dataframe_changelog.0', 'example_manifest/utils.get_dataframe_changelog.10', 'example_manifest/utils.get_dataframe_changelog.12', 'example_manifest/utils.get_dataframe_changelog.13']
- decorator_list: []
- type_params: []
- docstring: DataFrame changelog will be used as a UDF with spark,
so keeping it as a function that's not part of a class is preferred.

**docstring**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1453


#### example_manifest/utils.get_dataframe_changelog.0

**Call:**
- func: df.groupby
- args: ['time_col']
- keywords: ['example_manifest/utils.get_dataframe_changelog.0']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1454


#### example_manifest/utils.get_dataframe_changelog.1

**Call:**
- func: enumerate
- args: ['df_by_time']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1455


#### example_manifest/utils.get_dataframe_changelog.10

**Call:**
- func: diff_dfs.append
- args: ['example_manifest/utils.get_dataframe_changelog.10']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1456


#### example_manifest/utils.get_dataframe_changelog.11

**Call:**
- func: len
- args: ['diff_dfs']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1457


#### example_manifest/utils.get_dataframe_changelog.12

**Call:**
- func: pd.DataFrame
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1458


#### example_manifest/utils.get_dataframe_changelog.13

**Call:**
- func: pd.concat
- args: ['diff_dfs']
- keywords: ['example_manifest/utils.get_dataframe_changelog.13']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1459


#### example_manifest/utils.get_dataframe_changelog.2

**Call:**
- func: df_i.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1460


#### example_manifest/utils.get_dataframe_changelog.3

**Call:**
- func: inserted.rename
- args: []
- keywords: ['example_manifest/utils.get_dataframe_changelog.3']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1461


#### example_manifest/utils.get_dataframe_changelog.4

**Call:**
- func: diff_dfs.append
- args: ['example_manifest/utils.get_dataframe_changelog.4']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1462


#### example_manifest/utils.get_dataframe_changelog.5

**Call:**
- func: df_i.merge
- args: ['example_manifest/utils.get_dataframe_changelog.5']
- keywords: ['example_manifest/utils.get_dataframe_changelog.5', 'example_manifest/utils.get_dataframe_changelog.5', 'example_manifest/utils.get_dataframe_changelog.5']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1463


#### example_manifest/utils.get_dataframe_changelog.6

**Call:**
- func: example_manifest/utils.get_dataframe_changelog.6.0.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1464


#### example_manifest/utils.get_dataframe_changelog.6.0

**Call:**
- func: diff.query
- args: ['example_manifest/utils.get_dataframe_changelog.6.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1465


#### example_manifest/utils.get_dataframe_changelog.7

**Call:**
- func: diff_dfs.append
- args: ['example_manifest/utils.get_dataframe_changelog.7']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1466


#### example_manifest/utils.get_dataframe_changelog.8

**Call:**
- func: example_manifest/utils.get_dataframe_changelog.8.0.copy
- args: []
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1467


#### example_manifest/utils.get_dataframe_changelog.8.0

**Call:**
- func: diff.query
- args: ['example_manifest/utils.get_dataframe_changelog.8.0']
- keywords: []

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1468


#### example_manifest/utils.get_dataframe_changelog.9

**Call:**
- func: inserted.rename
- args: []
- keywords: ['example_manifest/utils.get_dataframe_changelog.9']

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.py
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/utils.py

**node:**
- connected_component_group: 1469


#### export_pbi_to_excel

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1470

**procedure**

**task**


#### export_report_data_products

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: pbi_workspace
- link_type: flow

**node:**
- connected_component_group: 1471

**task**


#### extracts_transfer_reports_to_fsmresfiles

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: fsmresfiles
- link_type: flow

**node:**
- connected_component_group: 1472

**task**


#### extracts_transfer_reports_to_teams

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: databricks_prd_catalog
- target: nunm_teams_sharepoint
- link_type: flow

**node:**
- connected_component_group: 1473

**task**


#### finalize_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/build_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1476


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None, 'nu_id [str]': None}

**foreign_keys:**
- nm_id: nm_role.nm_id
- nu_id: nu_role.nu_id

**node:**
- connected_component_group: 1477

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**name**

**node:**
- connected_component_group: 1478

**url**


#### get_feedback_on_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/build_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/constraints.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/workflow.yaml

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/intake_request.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**link:**
- source: irb_pbi_report
- target: pbi_report
- link_type: parent

**node:**
- connected_component_group: 24

**parent**

**path**


#### irb_report_code_product

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**link:**
- source: irb_report_code_product
- target: report_code_product
- link_type: parent

**node:**
- connected_component_group: 25

**parent**

**path**


#### logistical_training

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/constraints.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': 'Unique identifier.', 'identity_type [categorical]': {'description': 'Type of identity.', 'categories': ['employee', 'person_of_interest', 'b2b']}}

**node:**
- connected_component_group: 1486

**todo:** Do B2B accounts have an NM ID created for them? Is it their email?
- priority: 0.5


#### nm_data_portal

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1487


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None, 'pa_id [str]': 'If the user has a privileged access account.', 'job_code [str]': 'Unique identifier for their job.'}

**node:**
- connected_component_group: 1488


#### no_irb_test

**data_request:**
- requester_id: net002@ads.northwestern.edu

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/testcases.yaml

**node:**
- connected_component_group: 1489

**status**


#### noirb_pbi_report

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**link:**
- source: noirb_pbi_report
- target: pbi_report
- link_type: parent

**node:**
- connected_component_group: 24

**parent**

**path**


#### noirb_report_code_product

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**link:**
- source: noirb_report_code_product
- target: report_code_product
- link_type: parent

**node:**
- connected_component_group: 25

**parent**

**path**


#### northwestern_university_fsm_it

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1492


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'net_id [str]': 'Unique identifier for NU.'}

**node:**
- connected_component_group: 1493


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'patient_id [str]': 'The unique identifier for the patient, in combination with patient_id_type.\n', 'patient_id_type [categorical]': {'categories': ['nm_bi.ir_id', 'clarity.pat_id', 'mock.mock_id']}}

**node:**
- connected_component_group: 1497

**primary_key**

**primary_key**

**time_dependent**


#### pbi_app_homepage

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**node:**
- connected_component_group: 1498


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': None, 'description [str]': 'This description will show up in the portal.'}

**node:**
- connected_component_group: 24


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'user [person]': 'The user for the role.', 'workspace [workspace]': 'The PBI workspace in question.', 'role [categorical]': 'The PBI role.'}

**node:**
- connected_component_group: 1499


#### power_user_approval_process

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1500


#### power_user_office_hours

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1501


#### power_user_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: fsm_analyst_role.nm_id

**node:**
- connected_component_group: 1502


#### power_user_sharepoint

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1503

**url**


#### power_users_azdo_project

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1504


#### power_users_management_framework

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1506


#### ra_lib

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1508


#### ra_lib_repo

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**node:**
- connected_component_group: 1509

**repo:**
- url: https://NMHC@dev.azure.com/NMHC/FSM%20Research%20Analytics/_git/ra_lib


#### ra_reports

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1510


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'azdo_id [str]': 'Work item associated with this branch.', 'branch [git_branch]': 'The git branch component itself.'}

**foreign_keys:**
- azdo_id: data_request_work_item.id

**node:**
- connected_component_group: 1511


#### ra_reports_repo

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**node:**
- connected_component_group: 1512

**repo:**
- url: https://NMHC@dev.azure.com/NMHC/FSM%20Research%20Analytics/_git/ra_reports


#### ra_team_member_role

**compdef:**
- multiplicity: 0..*
- unparsed_fields: {'nm_id [str]': None}
- is_defined: True
- fields: {'entity': <Schema Field(name=entity, type=DataType(str))>, 'comp_key': <Schema Field(name=comp_key, type=DataType(str))>, 'nm_id': <Schema Field(name=nm_id, type=DataType(str))>}
- is_valid: True
- errors: 

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: fsm_analyst_role.nm_id

**node:**
- connected_component_group: 1513

**todo:** What *is* the data structure for identities? How do job codes, NM IDs, and security groups, and privileged access accounts fit together?

- priority: 0.5


#### recruitment_compliance_constraints

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1514

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': 'ID for the report, {irb_number}.{irb_rank:.02d} (e.g. STU001234.01)', 'irb_number [str]': 'IRB number for the study associated with the report.', 'irb_rank [int]': 'IRB rank is defined as the number of reports associated with a study at the time of request intake, counting the report itself. As such, IRB rank starts at 1 and increases in steps of 1. When doing a partition over irb_number ordered by created_date ascending this is the row number.\n', 'pbi_workspace [str]': 'Which Power BI workspace the report lives in.', 'inserted_datetime [timestamp]': 'Date when the report was created, i.e. the product_id was created and we started tracking report status.\n', 'data_steward_approval [bool]': 'Whether or not the data has been approved for release.', 'description [str]': 'Description for the report.'}

**node:**
- connected_component_group: 1516

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': None, 'filename [str]': None, 'notebook_type [categorical]': {'categories': ['etl', 'cohort', 'report']}, 'git_branch [str]': None}

**node:**
- connected_component_group: 25


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'azdo_id [str]': 'There is one and only one Azure DevOps work item per report configuration.\n', 'report_id [str]': 'ID of the report the Azure DevOps work item is associated with. For reports with IRBs this is based on the IRB number and the number of other reports for the same study. For reports without an IRB this is based on the Azure DevOps ID of the original work item.\n', 'irb_number [str]': 'Study number if provided, e.g. STU00000000.', 'assigned_to [str]': 'Individual the work item is assigned to.', 'domain [str]': 'Power BI Domain for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace [str]': 'Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'workspace_folder [str]': 'Folder in the Power BI workspace for the report. Also used when specifying the location of the report code in the reports repo.\n', 'report_dir_pattern [str]': 'Unix filename pattern specifying the directory inside the ra_reports repo that contains the report code.\n', 'azdo_title [str]': 'Title of the work item.', 'state [str]': "State of the work item, e.g. 'In Progress' or 'Closed'.", 'tags [str]': 'Tags associated with the work item.', 'predecessor_azdo_id [str]': "Azure DevOps work item ID of a predecessor linked in the work item. If a work item has a predecessor that is also a report work item (has the 'Report' tag), then the work item is an update to the original report.\n", 'is_active [str]': "If True, then this report is actively refreshed, using the metadata specified by this row. Each work item associated with a report can have an 'is_active' field in the yaml metadata, but only the most recent active work item (largest azdo_id with is_active == True) will be marked as active in this config table. When not specified, is_active defaults to True for work items with state == 'Closed'.\n", 'refresh_schedule [str]': 'Specification of how often the report should be executed.', 'irb_is_active [str]': 'For reports with an IRB, whether or not that IRB is active.', 'is_visible [str]': 'Whether or not any generated data should be visible to the end users.\n', 'description [str]': 'Description field for the work item. Some values have been extracted from her , e.g. irb_number.\n', 'is_valid [str]': 'If False, then some aspect of the work item is incorrectly defined, and this work item will not be used in production. Check the error_log field for details on the issue.\n', 'error_log [str]': 'Any recorded details on why a given work item may be invalid for specifying report metadata\n'}

**foreign_keys:**
- report_id: report.report_id
- azdo_id: data_request_work_item.id

**name**

**node:**
- connected_component_group: 1517

**primary_key**


#### report_delivery_is_efficient

**child**

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/requirements/functional.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}

**node:**
- connected_component_group: 1518

**path**


#### request_workflow

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/workflow.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nm_id [str]': None}

**foreign_keys:**
- nm_id: nm_compatible_role.nm_id

**node:**
- connected_component_group: 1519


#### research_analytics_azdo_project

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**node:**
- connected_component_group: 1521


#### research_analytics_infrastructure

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**infrastructure**

**node:**
- connected_component_group: 1522


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/infrastructure.yaml

**fields:**
- component: {'workspace_name [str]': 'E.g. "Research Core".', 'workspace_domain [str]': 'E.g. "Research IRB".', 'workspace_folders [list[str]]': 'E.g. "NUCATS, Study Tracker, FSMIT".', 'deployment_environment [categorical]': {'categories': ['dev', 'stg', 'prd']}}

**node:**
- connected_component_group: 1523


#### run_report

**code:**
- repo: ra_reports
- path: workflow/main.yaml

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**node:**
- connected_component_group: 8

**status**

**task**


#### set_report_access

**child**

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'report_id [str]': None, 'label [str]': {'description': 'Label for distinguishing different tables of the same report.', 'default': ''}}

**node:**
- connected_component_group: 1526

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/access.yaml

**fields:**
- component: {'nu_id [str]': None}

**foreign_keys:**
- nu_id: nu_role.nu_id

**node:**
- connected_component_group: 1528


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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'scd_type [str]': {'description': 'Slowly changing dimension type.', 'categories': ['Type 0', 'Type 1', 'Type 2', 'Type 3', 'Type 4']}}

**node:**
- connected_component_group: 1531


#### training_plan_for_stem_opt_students

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1532


#### training_process

**child**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/manage.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**node:**
- connected_component_group: 1534

**task**


#### updated_report_new_analyst_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/testcases.yaml

**node:**
- connected_component_group: 1535

**status**


#### updated_report_test

**data_request:**
- requester_id: net001@ads.northwestern.edu
- irb_number: STU00012345

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/testcases.yaml

**node:**
- connected_component_group: 1536

**status**


#### variable_naming_conventions

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/unsorted.yaml

**node:**
- connected_component_group: 1538


#### work_on_report

**description**

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/build_report.yaml

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
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/data.yaml

**fields:**
- component: {'worklog_id [int]': None, 'azdo_id [int]': None, 'user_id [str]': None, 'timestamp [timestamp]': None, 'duration [float]': None}

**foreign_keys:**
- azdo_id: azdo_work_item.id
- user_id: nm_account.nm_id

**node:**
- connected_component_group: 1539


#### write_report_to_catalog

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: databricks_prd_catalog
- link_type: flow

**node:**
- connected_component_group: 1540

**task**


#### write_report_to_sharepoint

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: nunm_teams_sharepoint
- link_type: flow

**node:**
- connected_component_group: 1541

**task**


#### write_report_to_volume

**entity_source:**
- source: user
- filename_pattern: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/**/*.yaml
- filename: /Users/zhafen/repos/iac-sketch/tests/test_data/example_manifest/meta/data/workflow/deliver_report.yaml

**link:**
- source: prd_ra_reports_cluster
- target: databricks_prd_volume
- link_type: flow

**node:**
- connected_component_group: 1542

**task**


