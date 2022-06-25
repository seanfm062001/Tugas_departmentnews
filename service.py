from nameko.rpc import rpc
import pickle
import dependencies

class RoomService:

    name = 'user_service'

    database = dependencies.Database()

    @rpc
    def add_user(self,username,password):
        add = self.database.add_user(username,password)
        return add

    @rpc
    def check_user(self,user_data):
        add = self.database.check_user(user_data)
        return add

    @rpc
    def set_session(self,user_data):
        add = self.database.set_session(user_data)
        return add

    @rpc
    def generate_session_id(self,user_data):
        add = self.database.generate_session_id()
        return add

    @rpc
    def delete_session(self,session_id):
        add = self.database.delete_session(session_id)
        return add

    @rpc
    def add_news(self,arrnamafile, text):
        add = self.database.add_news(arrnamafile, text)
        return add

    @rpc
    def edit_news(self,arrnamafile, text,newsid):
        add = self.database.edit_news(arrnamafile, text,newsid)
        return add

    @rpc
    def delete_news(self,newsid):
        add = self.database.delete_news(newsid)
        return add

    @rpc
    def get_news(self):
        add = self.database.get_news()
        return add

    @rpc
    def get_newsbyid(self,newsid):
        add = self.database.get_newsbyid(newsid)
        return add

    # @rpc
    # def get_all_room_type(self):
    #     room_types = self.database.get_all_room_type()
    #     return room_types
    
    # @rpc
    # def get_all_room(self):
    #     rooms = self.database.get_all_room()
    #     return rooms

    # @rpc
    # def get_numroom(self, nomer):
    #     number = self.database.get_numroom(nomer)
    #     return number
    
    # @rpc
    # def add_room(self,roomtype,roomnumber,status):
    #     add = self.database.add_room(roomtype,roomnumber,status)
    #     return add

    # @rpc
    # def update_room(self, nomor):
    #     nomorr = self.database.update_room(nomor)
    #     return nomorr

    # @rpc
    # def delete_room(self, numur):
    #     numurr = self.database.delete_room(numur)
    #     return numurr