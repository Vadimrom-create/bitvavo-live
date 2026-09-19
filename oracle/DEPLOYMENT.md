# Accès Oracle restreint via GitHub Actions

Ce canal ne donne jamais un shell SSH général à GitHub.

La clé dédiée est forcée côté serveur vers `/usr/local/sbin/bitvavo-deploy-gateway`.
Commandes autorisées uniquement :

- `health`
- `status`
- `restart`
- `logs`
- `deploy <sha-main>`

Le déploiement accepte uniquement un SHA présent dans l'historique de `main`,
compile le serveur Python avant installation, redémarre le service, vérifie
`http://127.0.0.1:8787/health` et restaure automatiquement la version précédente
si le healthcheck échoue.

## 1. Générer la clé dédiée sur le Mac

Ne pas réutiliser la clé SSH personnelle.

```bash
ssh-keygen -t ed25519 \
  -f ~/.ssh/bitvavo_oracle_deploy \
  -C github-actions-bitvavo-oracle \
  -N ''
```

Afficher uniquement la clé publique :

```bash
cat ~/.ssh/bitvavo_oracle_deploy.pub
```

Ne jamais coller le fichier sans suffixe `.pub` dans un chat ou un ticket.

## 2. Bootstrap unique sur Oracle

Se connecter au VPS avec le compte administrateur habituel, puis :

```bash
curl -fsSL \
  https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/main/oracle/bootstrap_oracle_deploy.sh \
  -o /tmp/bootstrap_oracle_deploy.sh
chmod 0700 /tmp/bootstrap_oracle_deploy.sh
```

Lancer ensuite le script en remplaçant le texte d'exemple par le contenu exact
de `~/.ssh/bitvavo_oracle_deploy.pub` :

```bash
sudo /tmp/bootstrap_oracle_deploy.sh 'ssh-ed25519 AAAA... github-actions-bitvavo-oracle'
```

Le script :
- crée `bitvavo-deploy` avec mot de passe verrouillé ;
- force la clé vers un gateway allowlisté ;
- interdit forwarding/PTTY/X11/agent forwarding ;
- installe un contrôleur root borné ;
- installe une règle sudo limitée à ce contrôleur ;
- affiche l'empreinte ED25519 du serveur.

## 3. Vérifier depuis le Mac

```bash
ssh -i ~/.ssh/bitvavo_oracle_deploy \
  -o IdentitiesOnly=yes \
  bitvavo-deploy@144.24.206.128 health
```

La réponse doit inclure un JSON de health du service.

Une commande arbitraire doit être refusée :

```bash
ssh -i ~/.ssh/bitvavo_oracle_deploy \
  -o IdentitiesOnly=yes \
  bitvavo-deploy@144.24.206.128 'uname -a'
```

Résultat attendu : `command not allowed`.

## 4. Construire la ligne known_hosts depuis le VPS

Sur Oracle :

```bash
sudo cat /etc/ssh/ssh_host_ed25519_key.pub
```

Si la sortie est par exemple :

```text
ssh-ed25519 AAAAC3... commentaire
```

la valeur GitHub doit être :

```text
144.24.206.128 ssh-ed25519 AAAAC3...
```

Comparer aussi l'empreinte avec celle affichée par le bootstrap.

## 5. Ajouter deux secrets GitHub

Repository :
`Vadimrom-create/bitvavo-live`

GitHub :
Settings -> Secrets and variables -> Actions -> New repository secret

### ORACLE_DEPLOY_SSH_KEY

Valeur = contenu complet de :

```bash
cat ~/.ssh/bitvavo_oracle_deploy
```

Cette valeur ne doit être copiée nulle part ailleurs.

### ORACLE_DEPLOY_KNOWN_HOSTS

Valeur = ligne construite à l'étape 4 :

```text
144.24.206.128 ssh-ed25519 AAAA...
```

## 6. Fonctionnement après bootstrap

### Déploiement

Toute modification validée de :

`oracle/bitvavo_public_probe.py`

sur `main` déclenche :

`.github/workflows/oracle_deploy.yml`

Le workflow :
1. compile le fichier ;
2. ouvre la connexion SSH restreinte ;
3. demande `deploy <GITHUB_SHA>` ;
4. le VPS vérifie que ce SHA appartient à `main` ;
5. sauvegarde l'ancien serveur ;
6. installe le nouveau ;
7. redémarre ;
8. healthcheck ;
9. rollback automatique si nécessaire.

### Contrôle à distance

Le workflow :

`.github/workflows/oracle_control.yml`

peut exécuter uniquement :
- health
- status
- restart
- logs

Un push de `oracle_control_request.json` contenant :

```json
{"action":"health","request_id":"example"}
```

déclenche le contrôle. Cela permet au dépôt de servir de canal d'administration
borné sans exposer un shell général.

## Sécurité

- dépôt public : aucune clé privée n'est stockée dans Git ;
- les secrets GitHub ne sont pas disponibles aux workflows provenant de forks ;
- la clé SSH elle-même est limitée par `authorized_keys` à cinq opérations ;
- le contrôleur revalide les arguments ;
- un déploiement ne peut cibler qu'un commit de `main` ;
- rollback automatique sur échec du healthcheck ;
- aucun accès Bitvavo privé n'est nécessaire à ce canal.
