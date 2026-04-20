from . import account, auth, ca, cert, find, forge, parse, relay, req, shadow, template

ENTRY_PARSERS = [
    account,
    auth,
    ca,
    cert,
    find,
    parse,
    forge,
    relay,
    req,
    shadow,
    template,
]

# ===== CUSTOM COMMANDS BEGIN =====
# Fork-local commands registered here. Do not edit outside this block when
# pulling upstream changes; merge conflicts will be confined to this region.
try:
    from .custom import CUSTOM_ENTRY_PARSERS

    ENTRY_PARSERS.extend(CUSTOM_ENTRY_PARSERS)
except Exception as _e:  # noqa: BLE001
    import sys

    print(f"[certipy-custom] failed to load custom parsers: {_e}", file=sys.stderr)
# ===== CUSTOM COMMANDS END =====
