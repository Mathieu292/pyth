#-*-coding:utf8-*

print("=== 1 Ajout d'un tache ===")
print("=== 2 Lister les taches ===")
print("=== 3 Marquer une taches comme terminer ===")
print("=== 4 Supprimer une tache ===")
print("=== 5 Quitter le programme ===")

Cont=True
def toDo():
    tasks=[]
    while Cont:
        choice=input("Enter a choice:")
        if choice == '1':
            task=input("Enter a task:")
            tasks.append(task)
        elif choice == '2':
            print("Tasks are",tasks)
        elif choice == '3':
            print("la tache est teminer")
        elif choice == '4':
            task=input("Enter a task:")
            tasks.remove(task)
        elif choice == '5':
            print("On quitte le programme")
            break

toDo()

