from logging import basicConfig, getLogger

basicConfig

logger = getLogger(__name__)

logger.error("Hello!")

def ohno():
    try:
        {}["cal_paterson"]
    except Exception:
        logger.exception("something went wrong here")

if __name__ == "__main__":
    for i in range(1):
        ohno()
