
from django.utils import timezone
from django.conf import settings
from blog.models import Post


def parse_datetime_input(s: str):
    s = s.strip()
    if not s:
        return None
    fmts = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d"]
    for f in fmts:
        try:
            dt = datetime.strptime(s, f)
            if getattr(settings, "USE_TZ", False):
                return timezone.make_aware(dt, timezone.get_current_timezone())
            return dt
        except ValueError:
            continue
    raise ValueError("Невідомий формат дати. Підтримувані формати: 'YYYY-MM-DD', 'YYYY-MM-DD HH:MM' або 'YYYY-MM-DD HH:MM:SS'")

# --- CRUD-процедури ---
def list_posts():
    posts = Post.objects.all().order_by("-published_date")
    if not posts:
        print("Немає постів у базі.")
        return
    print("\nСписок постів:")
    for p in posts:
        # локальний час для читабельності
        pd = p.published_date
        try:
            pd_str = timezone.localtime(pd).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pd_str = str(pd)
        print(f"ID: {p.id} | {p.title} | published: {pd_str}")

def add_post():
    title = input("Заголовок (title): ").strip()
    if not title:
        print("Title не може бути порожнім.")
        return
    print("Введіть текст поста (натисніть Enter, коли закінчили):")
    content = input("> ").strip()
    pd_input = input("Published date (YYYY-MM-DD [HH:MM[:SS]]) — залиште порожнім для тепер: ").strip()
    try:
        pd = parse_datetime_input(pd_input) if pd_input else timezone.now()
    except ValueError as e:
        print("Помилка:", e)
        return
    post = Post.objects.create(title=title, content=content, published_date=pd)
    print(f"Пост додано. ID = {post.id}")

def delete_post():
    list_posts()
    id_str = input("Введіть ID поста для видалення (або натисніть Enter щоб скасувати): ").strip()
    if not id_str:
        print("Скасовано.")
        return
    try:
        post_id = int(id_str)
    except ValueError:
        print("Невірний ID.")
        return
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        print("Пост з таким ID не знайдено.")
        return
    confirm = input(f"Видалити пост '{post.title}' (ID={post.id})? (y/N): ").strip().lower()
    if confirm == "y":
        post.delete()
        print("Пост видалено.")
    else:
        print("Скасовано.")

def view_post():
    list_posts()
    id_str = input("Введіть ID поста для перегляду (або Enter щоб вийти): ").strip()
    if not id_str:
        return
    try:
        post = Post.objects.get(pk=int(id_str))
    except Exception:
        print("Пост не знайдено.")
        return
    print("\n--- Пост ---")
    print("ID:", post.id)
    print("Title:", post.title)
    print("Published:", timezone.localtime(post.published_date) if post.published_date else "—")
    print("Content:\n", post.content)
    print("-----------\n")

def main():
    while True:
        print("\n=== Blog CLI ===")
        print("1. Перелік постів")
        print("2. Додати пост")
        print("3. Видалити пост")
        print("4. Переглянути пост")
        print("5. Вихід")
        choice = input("Вибір: ").strip()
        if choice == "1":
            list_posts()
        elif choice == "2":
            add_post()
        elif choice == "3":
            delete_post()
        elif choice == "4":
            view_post()
        elif choice == "5":
            print("Вихід.")
            break
        else:
            print("Невірний вибір. Спробуйте ще.")

if __name__ == "__main__":
    main()
