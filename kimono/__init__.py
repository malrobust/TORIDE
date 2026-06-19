from kimono.guard import AgentGuard, BlockedActionError
from kimono.policy import Action, Decision, PolicyEngine, Rule
from kimono.provenance import TRUST_LEVELS, Source, TaggedContent
from kimono.taint import TaintRegistry

try:
    from importlib.metadata import PackageNotFoundError, version

    try:
        __version__ = version("kimono-guard")
    except PackageNotFoundError:
        __version__ = "0.1.0"
except ImportError:
    __version__ = "0.1.0"

__all__ = [
    "__version__",
    "Source",
    "TaggedContent",
    "TRUST_LEVELS",
    "TaintRegistry",
    "Action",
    "Decision",
    "Rule",
    "PolicyEngine",
    "AgentGuard",
    "BlockedActionError",
]
