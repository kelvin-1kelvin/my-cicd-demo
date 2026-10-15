# NPG_temp.py  (Cloud Computing - Session 12: CI/CD - automating the path to
# production - STUDENT reproduce guide version)
# ============================================================================
# A tiny, deliberately boring function: given a temperature in Celsius, it
# returns whether it's Cold, Mild, or Hot. The point of this exercise isn't
# the function - it's building your own pipeline that tests it automatically
# on every push, and only "deploys" it if the tests pass.
#
# Safe by design: no network, no files, no storage - just plain Python.
# ============================================================================


def category(celsius):
    """Return Cold, Mild, or Hot for a Celsius temperature.

    Cold is below 15, Mild is 15 up to 28, Hot is 28 and above.
    """
    if celsius < 10:
        return "Cold"
    elif celsius < 28:
        return "Mild"
    else:
        return "Hot"
