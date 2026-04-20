"""Sessions helpers for course catalog and enrollment api."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def sessions_step_0(records: list[dict], limit: int = 109) -> list[dict]:
    """Apply sessions rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_1(records: list[dict], limit: int = 245) -> list[dict]:
    """Apply sessions rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_2(records: list[dict], limit: int = 48) -> list[dict]:
    """Apply sessions rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_3(records: list[dict], limit: int = 261) -> list[dict]:
    """Apply sessions rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_4(records: list[dict], limit: int = 485) -> list[dict]:
    """Apply sessions rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_5(records: list[dict], limit: int = 75) -> list[dict]:
    """Apply sessions rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sessions_step_6(records: list[dict], limit: int = 18) -> list[dict]:
    """Apply sessions rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sessions step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
