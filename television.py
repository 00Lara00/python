class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        This method initializes the instance variables.
        :status: False
        :muted: False
        :volume: Television.MIN_VOlUME
        :channel: Television.MIN_VOLUME
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This method turns the tv off and on.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute the volume
        :return: mute
        """
        if not self.__status:
            return
        elif not self.__muted:
            self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """""
        Method to decrease the tv channel>
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume.
        """
        if self.__status:
            self.__muted = False
            if self .__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """"
        Method to show the tv status.
        :return: tv status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
