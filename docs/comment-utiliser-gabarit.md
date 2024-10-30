# Comment Utiliser ce Gabarit

Pour utiliser ce gabarit comme base pour votre propre projet, suivez les étapes ci-dessous :

1. **Créer un Nouveau Dépôt Localement**

   ```sh
   mkdir mon-nouveau-repo
   cd mon-nouveau-repo
   ```

2. **Initialiser le Dépôt Git**

   - Initialisez un dépôt Git dans le nouveau répertoire. Assurez-vous que la branche principale soit nommée main et non master :

     ```sh
     git init -b main
     ```

   - Si main est déjà la branche principale par défaut, vous pouvez simplement initialiser le dépôt sans spécifier la branche.

     ```sh
     git init
     ```

3. **Récupérer le Code du Gabarit**

   - Récupérez le code de la branche main du gabarit à partir du dépôt GitHub :

     ```sh
     git pull https://github.com/arches-mcc/gabarit-python main
     ```

    > Note : L'utilisation de la commande `git pull` mentionnée ci-dessus va également récupérer l'historique des commits effectués dans le gabarit. Cela ne devrait pas poser de problème et est en fait tout à fait correct.

4. **Utiliser DevContainer**

   - Ouvrez le projet dans Visual Studio Code.
   - Si vous avez l'extension Remote - Containers installée, VS Code vous proposera d'ouvrir le projet dans un DevContainer. Acceptez cette proposition.

5. **Configurer bouton DevContainer**

   - Pour configurer le bouton qui lance le DevContainer dans VS Code directement à partir de GitHub pour votre nouveau répertoire, vous devez modifier la fin du lien pour qu'il redirige vers le nouveau dépôt. Par exemple, où il est écrit `/gabarit-python`, il devrait être `/nouveau-repo`.

   > Attention : Lors de l'utilisation du bouton, le DevContainer sera toujours ouvert sur la branche main. Assurez-vous que la branche main est correctement configurée pour le développement avec DevContainer.  Soyez attentif si votre travail doit être fait dans une autre branche.
