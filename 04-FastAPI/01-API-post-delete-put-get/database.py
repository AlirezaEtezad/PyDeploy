import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("TodoList.db")
        self.cursor = self.con.cursor()
    

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks
    
    
    def add_new_task(self, title, description, time, priority):
        try:
            query = f"INSERT INTO tasks (title, description, time, priority) VALUES('{title}', '{description}', '{time}', '{priority}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except sqlite3.IntegrityError as e:
            print("Integrity Error:", e)
            return False
        except sqlite3.Error as e:
            print("SQLite Error:", e)
            return False

    

    def remove_task(self, task_id):
        try:
            query = f"DELETE FROM tasks WHERE id={task_id}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def update_task(self, task_id, title, description, time, priority):
        try:
            query = f"UPDATE tasks SET title = '{title}', description = '{description}', time = '{time}', priority = '{priority}' WHERE id = {task_id}"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False 
