from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_id = member.get('id', self._generateId()) 
        member['id'] = member_id
        self._members.append(member)

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, member_id, updated_member):
        for member in self._members:
            if member['id'] == member_id:
                member.update(updated_member)
                return True
        return False

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None

    def get_all_members(self):
        return self._members

