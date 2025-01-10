from flask import Flask, jsonify
from flask_restful import Api, Resource
from db_connection import get_all_menu_items, get_menu_item_by_id, delete_menu_item

app = Flask(__name__)
api = Api(app)

class Menu(Resource):
    def get(self, id=None):
        if id is None:
            menu_items = get_all_menu_items()
            return jsonify(menu_items)

        menu_item = get_menu_item_by_id(id)
        if menu_item:
            return jsonify(menu_item)
        return {"message": "Item not found"}, 404

    # Можете проверить в постмане (Работает)
    def delete(self, id):
        if delete_menu_item(id):
            return {"message": f"Menu item with ID {id} deleted"}, 200
        return {"message": "Item not found"}, 404



api.add_resource(Menu,
                 "/api/v1.0/menu", # Смотрим на все
                 "/api/v1.0/menu/<int:id>") # Удаляем и смотрим по айди

if __name__ == "__main__":
    app.run(port=32000, debug=True)
