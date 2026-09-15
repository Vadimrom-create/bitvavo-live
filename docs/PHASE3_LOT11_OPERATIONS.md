# Phase 3 — exploitation du lot 11

## Producteurs et activation

| Chemin | Code et données | Sorties possédées |
|---|---|---|
| Prospection | SHA du workflow immuable ; état public lu dans un checkout de données distinct | Scan, état de sa data_policy, journaux V1/V2/comparaison, replay brut, manifeste |
| Monitoring | SHA explicitement validé par `config/monitor_release.json` ; état chiffré courant indépendant | État des livraisons, statut agrégé et disponibilité |
| Évaluation | SHA du workflow immuable ; journaux courants ; SQLite jetable | Rapports historiques/comparatifs, archives et manifeste d'évaluation |

Les listes `OWNERS` de `scripts/publish_data.py` sont disjointes. Les anciens répertoires `history/` et `decision_history/` n'ont aucun nouveau producteur. Le publisher prépare ses commits dans un worktree temporaire et conserve le HEAD du processus qui calcule. Il refuse tout conflit sur un même fichier produit, même si Git aurait pu fusionner deux lignes distinctes ; aucun force-push. Les sources immuables sont aussi protégées lors d'une publication portant sur un fichier isolé.

La prospection utilise explicitement `CORRECTED_INPUTS_V1`. Le mode de replay legacy reste disponible ; aucune formule V4 ni seuil n'est modifié. Les enrichissements diagnostiques ont une enveloppe de 120 secondes, avec priorité à la liste V4 à revalider. L'expiration empêche les nouvelles requêtes et conserve tous les marchés avec une cause d'indisponibilité. Cette enveloppe opérationnelle est distincte des seuils de décision et de la convention de disponibilité du comparateur.

Les runners shadow et le comparateur sont facultatifs et bornés ; leurs défaillances sont inscrites dans `shadow_status.json`. Le manifeste n'inclut que les sorties du scan explicite et ses états exacts. L'échec d'un shadow ne remplace pas un fichier courant par une ancienne sélection présentée comme fraîche. La page publique suit les manifestes ; les rapports historiques gardent leur propre date. Les replays bruts sont conservés dans `replay_history/`, en plus des artefacts CI temporaires.

Le chemin d'achat V4 exige un manifeste complet, frais (limite existante de 15 minutes), cohérent avec le payload lu, et un replay exact réussi. La santé globale du scan doit être OK. Les contrôles privés et leur fraîcheur restent obligatoires sur cette branche. `ALLOW_BUY_ALERTS` reste faux dans le workflow du monitoring. Une sortie de position justifiée ne lit pas ce manifeste d'achat.

## Mesures et limites connues

Les mesures distinguent durée d'acquisition du compte, évaluation des positions, âge du compte/carnet, couverture réellement fraîche, contrôle final avant SMTP et intervalles d'évaluations réussies. Le timestamp serveur du contenu reste nul lorsqu'il n'est pas fourni ; la date HTTP n'est pas inventée comme timestamp du carnet. Une absence de données de trailing requises ne compte pas comme supervision complète, mais n'empêche pas la livraison d'une autre sortie justifiée.

`monitor_availability.json` ne contient ni actifs détenus, ni soldes, ni identifiants d'ordre. Il conserve sept jours d'observations agrégées et les états UNCONFIGURED/erreur. Le contrôle SLO n'est possible qu'après une fenêtre observée complète : p95 ≤ 300 secondes et interruption maximale ≤ 600 secondes. L'intervalle entre observations ne prouve pas une disponibilité continue entre celles-ci.

État réel constaté sur main le 13 septembre à 18:37 UTC : `UNCONFIGURED`, raison `READ_ACCOUNT_OR_ENCRYPTION_SECRET_MISSING`, gestion des positions bloquée. Les validations du compte, des plans réels, des permissions read-only, de la fraîcheur en situation réelle et de la livraison SMTP restent **PENDING PRIVATE CONFIGURATION**. Aucun secret n'a été demandé ni lu pour ces tests ; tous les transports de tests sont simulés.

Les cinq intervalles récents de workflows de prospection observés sont de l'ordre de 13 à 20 minutes. Ce ne sont pas des mesures de supervision privée. Aucun respect de la cible de cinq minutes n'est démontré. Les cron du monitoring ne sont pas multipliés. Si une période réelle échoue au SLO, le seul changement à préparer est l'hébergement/déclenchement du code de monitoring validé, avec l'état chiffré courant et un expéditeur unique ; aucun nouvel hôte n'est présumé disponible.

## Rollback et reprise

1. Index corrompu : laisser le runner isoler uniquement la base dérivée puis reconstruire depuis les journaux ; une divergence de journal reste une erreur, pas un prétexte à le remplacer.
2. Publication conflictuelle : conserver les sources/artefacts et reprendre le cycle depuis l'état public réellement courant. Ne jamais forcer le push ni fusionner automatiquement deux états produits.
3. Achat ou manifeste douteux : achats désactivés, monitoring des positions conservé.
4. Monitoring : revenir au dernier SHA validé avec l'état chiffré et les identifiants de livraison les plus récents, jamais avec une ancienne copie de l'état privé. Après acquittement SMTP et échec de persistance, conserver le statut d'incertitude ; aucune garantie « exactement une fois ».
5. Évaluation : désactiver son workflow/rapport si nécessaire ; ses journaux d'entrée restent intacts.

Le pin du monitoring est un commit de métadonnées suivant le commit de code testé : un commit ne peut pas contenir son propre SHA. Aucune promotion de DL-V2 et aucun lancement du pilote de l'étape 12 ne sont inclus dans ce lot.

## Clôture locale du lot 11 — 14 septembre 2026

Référence avant lot : `a7c5d6f9281535bc870359f98e0f66f3c1bcf9b1`, branche `codex/astra-phase3-20260911`. Inspection finale des 32 fichiers du lot : aucune correction de code supplémentaire nécessaire à cette reprise. Quatre fichiers avaient changé depuis la précédente suite complète ; la version finale a donc été retestée : `python3 scripts/run_tests.py all`, **139 tests réussis**, dont intégration collecte/replay/shadows/manifeste/publication sur dépôt distant local et évaluation séparée. Un premier lancement avait échoué à importer `requests` ; les dépendances déclarées dans `executor/requirements.txt` ont été réinstallées sans modification du repository.

Les quatre workflows concernés sont syntaxiquement lisibles en YAML. `git diff --check` est sans erreur. Les objets protégés par `config/phase3_reference.json` sont inchangés : V4 gelée, seuils, règles, pondérations, DL-V1 et références historiques. Les replays historiques précédemment validés ne sont pas relancés ; les replays exacts sur fixtures des deux chemins de données passent dans la suite finale.

La parité historique déjà obtenue est conservée sans recalcul exhaustif : l'empreinte des 197 journaux est toujours `48102b4b1839cde62bfd405d4688f12b0d02ca4b70e2c936292770c928636151`, identique au manifeste de la validation incrémentale/reconstruction. L'archive `history/2026-09-08/20260908T205101Z-34cfba07.json.gz` est identique à HEAD, gzip valide, SHA-256 `3a391a8f56ac8d0a8387cb08742c3975e47b568c056baeb76ede4247f55edc66` ; elle est exclue du diff et du commit.

Ce checkpoint est un commit local de code testé, sans publication ni activation d'un nouveau SHA de monitoring. Le pin existant reste en place. Les tests locaux ne constituent pas des runs CI distants ni une validation privée Bitvavo. **Étape 12 non commencée.**
