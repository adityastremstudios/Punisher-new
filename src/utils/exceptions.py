from discord.ext import commands


class PunisherError(commands.CheckFailure):
    pass


class NotSetup(PunisherError):
    def __init__(self):
        super().__init__(
            "This command requires you to have Punisher's private channel.\nKindly run `{ctx.prefix}setup` and try again."
        )


class NotPremiumGuild(PunisherError):
    def __init__(self):
        super().__init__(
            "This command requires this server to be premium.\n\nCheckout Punisher Premium [here]({ctx.bot.prime_link})"
        )


class NotPremiumUser(PunisherError):
    def __init__(self):
        super().__init__(
            "This command requires you to be a premium user.\nCheckout Punisher Premium [here]({ctx.bot.prime_link})"
        )


class InputError(PunisherError):
    pass


class SMNotUsable(PunisherError):
    def __init__(self):
        super().__init__("You need either the `scrims-mod` role or `Manage Server` permissions to use this command.")


class TMNotUsable(PunisherError):
    def __init__(self):
        super().__init__("You need either the `tourney-mod` role or `Manage Server` permissions to use tourney manager.")


class PastTime(PunisherError):
    def __init__(self):
        super().__init__(
            f"The time you entered seems to be in past.\n\nKindly try again, use times like: `tomorrow` , `friday 9pm`"
        )


TimeInPast = PastTime


class InvalidTime(PunisherError):
    def __init__(self):
        super().__init__(f"The time you entered seems to be invalid.\n\nKindly try again.")
