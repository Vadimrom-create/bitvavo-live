"""Optional full shadow/publication gate, outside the acquisition gate."""
import test_pipeline_replay


class ShadowPublicationIntegration(test_pipeline_replay.PipelineReplayTests):
    include_shadow_publication = True
