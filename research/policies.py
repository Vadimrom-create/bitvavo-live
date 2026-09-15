"""Functional identities are independent of the executing Git revision."""
FROZEN_V4 = 'V4_FROZEN_20260908'
FROZEN_DL1 = 'DECISION_LAYER_V1_SHADOW'
CANDIDATE = 'DL_V2_OPPORTUNITY_BASELINE_SHADOW'
LEGACY_DATA = 'LEGACY_OBSERVED_V1'
CORRECTED_DATA = 'CORRECTED_INPUTS_V1'
EXECUTION = 'READ_ONLY_ALERTS_V1'
EVALUATION = 'PROSPECTIVE_PAIRED_V1'


def identities(*, data_policy=CORRECTED_DATA, decision_policy=FROZEN_V4,
               execution_policy=EXECUTION, evaluation_policy=EVALUATION):
    return dict(data_policy=data_policy, decision_policy=decision_policy,
                execution_policy=execution_policy, evaluation_policy=evaluation_policy)

LEGACY_DIAGNOSTICS = 'LEGACY_V4_CORRECTED_DIAGNOSTICS_V1'
