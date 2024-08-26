import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import TodoItem
from app.crud import create_todo, get_todo_by_id, update_todo_by_id, delete_todo_by_id


@pytest.fixture(scope="module")
async def test_db():
    client = AsyncIOMotorClient("mongodb://username:password@localhost:27017")
    db = client.test_database
    global todo_collection
    todo_collection = db.todos
    yield db
    await client.drop_database("test_database")
    client.close()


@pytest.fixture
def todo_data():
    return TodoItem(title="Test Todo", description="Test Description")


@pytest.mark.asyncio(loop_scope="module")
async def test_create_todo_item(test_db, todo_data):
    new_todo = await create_todo(todo_data)
    assert new_todo["title"] == todo_data.title
    assert new_todo["description"] == todo_data.description
    assert new_todo["completed"] is False


@pytest.mark.asyncio(loop_scope="module")
async def test_read_todo_item(test_db, todo_data):
    new_todo = await create_todo(todo_data)
    assert new_todo["title"] == todo_data.title


@pytest.mark.asyncio(loop_scope="module")
async def test_update_todo_item(test_db, todo_data):
    new_todo = await create_todo(todo_data)
    updated_todo = await update_todo_by_id(str(new_todo["_id"]), {"completed": True})
    assert updated_todo["completed"] is True


@pytest.mark.asyncio(loop_scope="module")
async def test_delete_todo_item(test_db, todo_data):
    new_todo = await create_todo(todo_data)
    await delete_todo_by_id(str(new_todo["_id"]))
    todo = await get_todo_by_id(str(new_todo["_id"]))
    assert todo is None
