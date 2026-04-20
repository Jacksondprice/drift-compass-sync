"""Metrics helpers for course catalog and enrollment api."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def metrics_step_0(records: list[dict], limit: int = 189) -> list[dict]:
    """Apply metrics rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_1(records: list[dict], limit: int = 27) -> list[dict]:
    """Apply metrics rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_2(records: list[dict], limit: int = 450) -> list[dict]:
    """Apply metrics rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_3(records: list[dict], limit: int = 388) -> list[dict]:
    """Apply metrics rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_4(records: list[dict], limit: int = 47) -> list[dict]:
    """Apply metrics rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_5(records: list[dict], limit: int = 314) -> list[dict]:
    """Apply metrics rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_6(records: list[dict], limit: int = 339) -> list[dict]:
    """Apply metrics rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_7(records: list[dict], limit: int = 290) -> list[dict]:
    """Apply metrics rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_8(records: list[dict], limit: int = 214) -> list[dict]:
    """Apply metrics rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_9(records: list[dict], limit: int = 469) -> list[dict]:
    """Apply metrics rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def metrics_step_10(records: list[dict], limit: int = 225) -> list[dict]:
    """Apply metrics rule 10 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("metrics step 10 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
