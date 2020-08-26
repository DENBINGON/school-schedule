#!/bin/bash
# -*- utf-8 -*-

# Импорт библиотек
import vk_api, random
from modules import const, db
from modules.bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType


# Основной класс
class SchoolScheduleMainApp( ):
    def __init__ ( self ):

        self.session = vk_api.VkApi( token=const.__TOKEN_APP__ )

        self.session._auth_token( )

        self.longpoll = VkLongPoll( self.session )
        self.DBMethods = db.dataBaseMethods( )

        for event in self.longpoll.listen( ):
            try:
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        if self.DBMethods.anotherInfoGet( event.user_id ) == False:
                            print( f'New message -> For me by: {event.user_id} -> Text: {event.text} \n', end='' )
                            bot = VkBot( event.user_id )
                            answer, userCode = bot.MessageParcer( event.text )
                            if userCode == 1:
                                self.WriteMessage( event.user_id, answer )
                            else:
                                if self.DBMethods.checkUser( event.user_id ) == True:
                                    self.DBMethods.removeUser( event.user_id )
                                    self.DBMethods.addNewUserInformation(
                                        self.getUserInformation( event.user_id )[ 0 ] )
                                    answer, userCode = bot.MessageParcer( event.text )
                                    self.WriteMessage( event.user_id, answer )
                                else:
                                    self.DBMethods.addNewUserInformation(
                                        self.getUserInformation( event.user_id )[ 0 ] )
                                    answer, userCode = bot.MessageParcer( event.text )
                                    self.WriteMessage( event.user_id, answer )
                        else:
                            pass
            except:
                continue

    def WriteMessage ( self, user_id, message ):
        self.session.method( 'messages.send',
                             { 'user_id': user_id, 'message': message, 'random_id': random.random( ) * 1000,
                               'keyboard': const.__KEYBOARD__ } )

    def getUserInformation ( self, user_id ):
        return self.session.method( 'users.get',
                                    { 'user_id': user_id, 'random_id': random.random( ) * 1000 } )

# Запускаем
if __name__ == "__main__":
    start = SchoolScheduleMainApp( )
