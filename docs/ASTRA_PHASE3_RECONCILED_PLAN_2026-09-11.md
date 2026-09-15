# Arbitrage contradictoire et plan final réconcilié de phase 3

Date : 11 septembre 2026. Repository : `Vadimrom-create/bitvavo-live`.

**Décision générale.** Conserver les corrections démontrées et les invariants du plan de phase 2, réduire ses prérequis non indispensables, et rendre explicitement expérimentaux les changements de décision. Aucune amélioration de performance n’est présumée.

**Aucun fichier du repository n’a été modifié, aucun commit créé, aucun seuil changé et aucun correctif implémenté pendant cet arbitrage.** Seul ce document de restitution est créé. L’ancienne copie locale tronquée du journal signalée dans l’audit est laissée inchangée.

## Vérifications utilisées pour l’arbitrage

J’ai relu intégralement [l’audit initial](sandbox:/workspace/scratch/24820e787d8c/ASTRA_AUDIT_REPORT_2026-09-10.md) et [le plan complet de phase 2](sandbox:/workspace/scratch/24820e787d8c/ASTRA_PHASE2_CORRECTION_PLAN_2026-09-10.md). Les objections fournies ont été confrontées aux preuves, sans validation préalable de leur bien-fondé.

Le code actuel est vérifié à [`1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2`](https://github.com/Vadimrom-create/bitvavo-live/commit/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2), commit du 11 septembre à 06:18:06 UTC. Les [70 commits depuis la référence de phase 2](https://github.com/Vadimrom-create/bitvavo-live/compare/e5def881ecfd30921d72b9b82ae21c43c181aed4...1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2) changent les données et sorties, pas les sources ou workflows concernés.

Les sources locales utilisées ont été rapprochées des empreintes Git actuelles ; le workflow et le script de publication plus récents ainsi que les fichiers DL absents de l’ancien checkout ont été lus à la révision distante fixée.

Le dernier scan, `20260911T061509Z-0eb80f02`, a été rejoué avec le code DL actuel après vérification des empreintes de ses deux journaux compressés : **430 observations, aucun écart sur les huit champs de résultat produits par `decide`, six tests DL existants réussis**. La décision est générée à 06:18:01,823 pour un scan horodaté 06:16:31,859, soit **89,96 secondes plus tard**. Cela confirme la fidélité du replay, pas la validité des entrées ni une supériorité de la politique. [Journal du scan](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/history/2026-09-11/20260911T061509Z-0eb80f02.json.gz), [journal DL](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/decision_history/2026-09-11/20260911T061509Z-0eb80f02.json.gz).

Ce même scan comporte quatre observations satisfaisant tous les contrôles qualité. Le rapport publié contient désormais 83 662 observations, 4 438 résultats complets à quatre heures et 79 224 censurés ; ces agrégats récents sont lus dans le rapport, sans nouvelle reconstruction exhaustive. Le monitoring reste `UNCONFIGURED`, `READ_ONLY`, achats bloqués faute de configuration. [Évaluation publiée](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/evaluation.json), [statut du monitoring](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/position_monitor_status.json).

Les 113 scans et 29 replays du premier audit restent les preuves historiques déjà établies. Ils ne sont pas présentés comme de nouveaux essais ni comme un held-out. La limite du replay V4 brut précédemment confirmée par CI, sans réexécution locale de son archive inaccessible lors de l’audit, demeure distincte du replay DL effectué ici.

## Arbitrage des neuf objections

### 1. Limiter l’investissement dans l’ancien exécuteur — ACCEPTÉE

A1 établit une publication privée insuffisamment filtrée. A2 établit un plafond cumulé non appliqué, surtout critique en cas de réactivation. Le chemin `security_event` peut en outre annuler un ordre via une option indépendante du `dry_run` de l’achat : une simple consigne de dry-run ne suffit pas à démontrer la fermeture complète. [Code de l’exécuteur](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/executor/daemon.py).

La phase 2 autorisait déjà le report du registre d’exposition, mais son étape finale 2 demandait encore de le tester immédiatement. Cette incohérence est corrigée : liste blanche publique et blocage central des mutations maintenant ; registre transactionnel complet dans un lot distinct seulement si une réutilisation devient nécessaire. La fermeture du daemon réellement déployé doit rester vérifiable.

### 2. Réduire le contrat temporel préalable à A3/A4 — ACCEPTÉE AVEC MODIFICATION

Les métadonnées de début/réception et la réponse sont déjà enregistrées par `PublicClient`. Une refonte générale n’est pas nécessaire pour réparer les caches. En revanche, `ReplayClient` écrase par clé URL/paramètres les réponses antérieures. Un renouvellement après clôture pourrait donc contaminer le replay de la consommation antérieure si l’on reportait toute la liaison des réponses. [Transport et replay](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/research/http.py).

Je sépare le noyau indispensable — contenu/métadonnées cohérents, identité des réponses consommées, cutoff, fraîcheur par profil — de la traçabilité complémentaire. A3/A4 sont livrés avec ce minimum et leurs reproductions, sans attendre une architecture de provenance enrichie. Reporter l’enrichissement de traçabilité est accepté ; reporter la correction nécessaire au replay est refusé.

### 3. Versionner explicitement `data_policy` — ACCEPTÉE

Le plan distinguait déjà entrées et décision, mais utilisait `input_policy` sans contrat d’identité suffisamment explicite. Réparer le cache journalier ou la clôture 15 minutes change les données fournies au moteur, même si les formules V4 restent identiques. [Cache journalier](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/v4_common.py), [consommation des bougies](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/pipeline.py).

`data_policy` devient explicite et distinct de `decision_policy`, `execution_policy`, `evaluation_policy` et du SHA. Les comparaisons distinguent une même politique sur données anciennes/corrigées et plusieurs politiques sur données corrigées communes. L’historique n’est pas artificiellement enrichi après coup et les interactions données/décision interdisent une attribution additive automatique.

### 4. Opportunity seul comme baseline expérimentale — ACCEPTÉE

L’audit B4 démontre un recouvrement entre facteurs, pas que ce recouvrement est nécessairement défavorable. Le code Opportunity incorpore déjà Trend à 23 % ou 68 % selon le chemin retenu ; supprimer les termes ajoutés par DL‑V1 ne produit donc pas un score indépendant ou optimal. [Calcul Opportunity](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/v4_detector.py#L211), [rang DL‑V1](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/research/decision_layer.py#L79).

Le classement simple est conservé sous identité de baseline shadow. Aucun gain ne lui est attribué avant comparaison prospective. Une amélioration de V2 complète n’isole pas l’effet du ranking si qualité et catégories changent aussi ; cette attribution demanderait une ablation à admissibilité constante.

### 5. Ne pas activer les nouvelles heuristiques support/reprise — ACCEPTÉE

Le support existant est une feature descriptive, et `plan` utilise actuellement l’ask comme prix d’entrée. Ni « limite au support » ni « clôture au-dessus de la bougie précédente » ne découle nécessairement de la correction des catégories. Ce sont de nouvelles hypothèses de timing et d’exécution. [Features](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/research/features.py), [plan de risque](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/research/risk.py).

La phase 2 prévoyait déjà V2 en shadow, mais sa description des promotions pouvait donner à ces deux règles une autorité excessive. Elles deviennent des expériences optionnelles séparées, avec plans ex ante et absence de route vers les achats actifs. Leur utilité reste à tester en shadow ; l’acceptation porte sur cette limitation, pas sur leur efficacité supposée.

### 6. Réviser le dimensionnement 5 % / 80 % / cinq points — ACCEPTÉE AVEC MODIFICATION

Les anciennes observations très censurées et dépendantes ne permettent pas de justifier une taille d’échantillon par nombre de scans. La phase technique doit renseigner les épisodes utiles, les différences appariées, leurs dépendances et la disponibilité des labels.

Cependant, variance et fréquence des épisodes ne déterminent pas à elles seules le risque d’erreur acceptable, la puissance souhaitée ou le gain minimal utile. Ces choix doivent être justifiés avant le held-out ; ils ne doivent pas être sélectionnés parce qu’ils rendent le résultat du pilote favorable. Les trois nombres deviennent des scénarios de dimensionnement possibles, pas des critères imposés. Le minimum de trente jours est conservé comme plancher calendaire, sans promesse de puissance ni de représentativité.

### 7. Comparaison commune et comparaison native end-to-end — ACCEPTÉE AVEC MODIFICATION

La phase 2 prévoyait déjà une comparaison commune et une lecture de latence. L’objection améliore le plan en exigeant une deuxième comparaison complète incluant les conséquences du délai : occasions perdues, indisponibilités, admissibilité restante et scénarios économiques identifiables. Les 89,96 secondes observées sur le dernier replay confirment que l’horodatage du scan ne peut représenter la disponibilité DL.

Je distingue le cutoff d’information et l’heure d’exécution. La convention de disponibilité commune appartient au comparateur ; elle ne retarde pas V4 en exploitation. La comparaison native utilise le chemin observé de chaque politique, sans lui prêter des entrées ou une publication plus précoces. Elle conserve la même référence d’événement pour ne pas effacer les mouvements manqués en déplaçant le label.

### 8. Séparer FN end-to-end et FN décisionnels conditionnels — ACCEPTÉE AVEC MODIFICATION

Le problème est réel : quatre observations sur 430 satisfont les contrôles globaux du dernier scan, tandis qu’un statut de collecte `OK` ne dit pas quelles capacités restent exploitables. La séparation permet de localiser les pertes sans assimiler toute indisponibilité à une décision de veto injustifiée.

Le masque d’exploitabilité sera défini ex ante par capacité, sans dépendre du classement ni du résultat. Les FN conditionnels seront accompagnés du dénominateur, de la couverture et du bilan end-to-end incluant les abstentions. Une sélection correcte perdue à la publication sera attribuée à l’intégration, pas au classement. Les deux nombres ne s’additionnent pas. Un label inconnu reste censuré ; un manque de données concomitant n’est pas une preuve causale que sa correction aurait sauvé le signal. Le contrôle d’exploitabilité ne doit pas devenir une façon de retirer du bilan les marchés difficiles.

### 9. Mesurer la cadence utile et reconnaître les limites de GitHub — ACCEPTÉE

Cette orientation est déjà présente en P4.3. Je la conserve et précise l’objet mesuré : évaluations de positions réellement réussies, âge du compte/carnet à la décision, couverture et interruptions, puis décomposition des causes. Les intervalles du premier audit concernaient les déclenchements, alors que le monitoring publié reste non configuré.

Le workflow actuel utilise déjà un cron décalé, `2-59/5`. GitHub documente les retards et suppressions possibles sous charge. Une multiplication des cron ne remplace pas une mesure ; en cas d’exigence non satisfaite, seul le chemin critique sera déplacé vers un environnement approprié avec le même code validé. [Workflow actuel](https://github.com/Vadimrom-create/bitvavo-live/blob/1a943bf0adc3bbfe266f6e2b60c1610f05be5ee2/.github/workflows/update.yml), [documentation GitHub](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

**Bilan des décisions : cinq objections ACCEPTÉES, quatre ACCEPTÉES AVEC MODIFICATION.** Aucune n’est rejetée en bloc. Cela ne valide aucune hypothèse de rendement : le classement Opportunity seul et les règles support/reprise restent des expériences, avec une efficacité non établie.

## Ce qui reste inchangé et ce qui change dans P0–P4

| Partie | Conservé | Modification retenue |
|---|---|---|
| P0.1 — A1 | Liste blanche publique, détails privés, contrôle du déploiement, rollback sans fuite | Aucune modification de fond |
| P0.2 — A2 | Fermeture de toutes les mutations et refus sur état inconnu | Registre complet et tests d’exposition différés ; retrait de l’obligation immédiate dans la séquence finale |
| P0.3 — A5 | Monitoring indépendant, SHA validé, état courant, sorties prioritaires, un seul expéditeur | Aucune modification de fond ; mesure de cadence commencée dès ce lot |
| P1.1 | Identité des entrées, causalité temporelle et replay exact | Noyau local indispensable puis complément ciblé ; `data_policy` et identités explicites |
| P1.2–P1.3 — A3/A4 | Cache par profil, clôture source, paramètres existants, reproduction des défauts | Dépendent du minimum temporel, sans attendre toute la traçabilité ; fraîcheur des dépendances et portée de l’heure HTTP explicitées |
| P1.4–P1.6 — A6/A7 | Capacités par usage, inconnus, spread monotone, vrais statuts de mèches, vue V1 préservée | Interprétations attribuées à leurs versions de données/décision ; aucune pénalité nouvelle présumée valide |
| P1.7 — A8 | Fallback, rejets locaux/globaux, une seule proposition, priorité aux ventes, déduplication | Aucune modification de fond |
| P1.8–P1.9 — A9/A10 | Continuité complète et séparation courant/historique | Aucune modification de fond |
| P2 | V2 séparée en shadow, mêmes valeurs de seuils, IOST réel distinct du synthétique, catégories cohérentes | Opportunity explicitement baseline ; support/reprise optionnels et isolés, sans promotion active par héritage |
| P3 | Comparaison prospective, événements/épisodes, censure, frais, plans ex ante, held-out neuf, absence de fuite | Deux comparaisons complètes, attribution à `data_policy`, deux FN avec dénominateurs, dimensionnement justifié après pilote |
| P4 | Trois chemins, publication cohérente, code immuable, état chiffré, index reconstructible | Cadence centrée sur les décisions réussies et l’âge des données ; aucune complexification de cron comme substitut |

## Invariants applicables à tous les lots

- Sources figées V4 et comportement DL‑V1 reproductibles ; mêmes entrées et état donnent les mêmes sorties historiques. Changer les données est une nouvelle variante identifiée, pas une falsification de la baseline.
- Journaux first-seen immuables ; annotations correctives séparées et datées ; absence de réécriture rétrospective des observations ou des labels anciens sous une identité inchangée.
- Aucun seuil, poids ou filtre optimisé à partir d’IOST, du pilote ou du held-out pour obtenir un résultat souhaité. Les correctifs d’interface sont distingués des nouvelles hypothèses de décision.
- Monitoring en lecture seule ; aucune nouvelle exécution automatique ; priorité vente → profits partiels → trailing → achat ; stop proposé jamais abaissé.
- Sortie justifiée possible avec compte/plan/carnet valides même si la prospection ou les bougies nécessaires au trailing sont indisponibles. Les données indispensables à cette sortie restent exigées.
- Une seule nouvelle proposition d’achat par cycle, contraintes de portefeuille conservées, déduplication et marquage de livraison après succès SMTP. L’incertitude SMTP accepté/persistance échouée n’est pas transformée en garantie de livraison exactement une fois.
- Confidentialité publique, code testé identifiable, pas de force-push ni d’écrasement automatique des conflits ; le code exécuté ne change pas lors du rebase de publication.
- Un test ou un replay réussi établit un comportement reproductible. Un meilleur rappel ne démontre pas une meilleure rentabilité. Aucune probabilité de hausse calibrée n’est produite sans validation propre.

## Plan réconcilié détaillé P0–P4

Les sections suivantes reprennent les exigences de phase 2 conservées et intègrent les arbitrages ci-dessus. Les chemins nouveaux désignent des travaux futurs, non des fichiers déjà implémentés.

## P0 — À corriger immédiatement

### P0.1 — Confidentialité de l’ancien exécuteur — A1

**Cause racine.** Des objets issus de l’activité privée sont publiés après un filtrage insuffisant. Leur nom `safe_event` ne constitue pas une garantie de confidentialité.

**Correction minimale recommandée.**

1. Remplacer la publication de ces objets par un schéma public à liste blanche : disponibilité, mode, gel de sécurité, horodatage et code générique d’état.
2. Exclure identifiants d’ordres, marchés, sens, quantités, prix, identifiant opérateur et résultats détaillés d’approbation.
3. Conserver les détails uniquement dans le journal privé.
4. Vérifier que le processus réellement déployé utilise cette correction : modifier GitHub seul ne suffit pas si un ancien daemon continue de publier.

**Fichiers et fonctions.** `executor/daemon.py` : `publish_status`, `security_event`, `_publish_github_json`. Ajouter `tests/test_executor_safety.py`.

**Tests et critère d’acceptation.**

- Injecter des événements contenant des valeurs sentinelles, y compris dans des dictionnaires imbriqués et des messages d’erreur.
- Intercepter toutes les publications publiques.
- Exiger **zéro valeur privée et zéro champ hors liste blanche** dans les payloads et logs publics.
- Vérifier séparément que le journal privé conserve les détails nécessaires.

**Régression / compatibilité.** Les consommateurs du statut public peuvent perdre des champs. Le schéma devra être versionné ; la compatibilité ne justifie pas de conserver une fuite.

**Dépendance / ordre.** Premier correctif, indépendant des travaux de décision.

**Rollback.** Désactiver la publication du statut concerné. Ne pas rétablir l’ancien sérialiseur.

**Limite à traiter explicitement.** L’arrêt des publications ne retire pas les données présentes dans les anciennes révisions publiques. Leur retrait éventuel constitue une opération distincte à préparer, sans toucher aux journaux historiques de marché ni prétendre qu’une suppression du dernier fichier suffit.

### P0.2 — Fermeture immédiate de l’ancien exécuteur ; infrastructure différée — A2

**Cause racine conservée.** `max_total_new_exposure_eur` est configuré sans intervenir dans la validation. Le contrôle par ordre ne remplace pas un plafond cumulé. Le chemin secondaire d’annulation d’un ordre inconnu n’est pas protégé par le seul `dry_run` du chemin d’achat.

**Périmètre immédiat de phase 3.**

- Bloquer centralement toute création, modification ou annulation automatique d’ordre, y compris les chemins secondaires.
- Refuser une activation implicite par configuration absente, état illisible ou redémarrage. Un état inconnu ne devient pas un état vide autorisant l’exécution.
- Conserver les lectures et les diagnostics privés nécessaires, sans développer un nouvel automate d’exécution.
- Identifier et vérifier le processus effectivement déployé avant de déclarer le blocage opérationnel acquis.

**Fichiers.** `executor/daemon.py`, `executor/bitvavo_client.py`, nouveau `tests/test_executor_safety.py`.

**Acceptation immédiate.** Les tests interceptent le transport et prouvent zéro mutation sortante pour achat, modification, annulation explicite, annulation secondaire, redémarrage et état invalide. Le statut public ne prétend pas que le plafond cumulé est implémenté.

**Travail différé, hors chemin critique de cette phase 3.** Si une réutilisation de cet exécuteur devient nécessaire, un lot distinct devra traiter le plafond et le registre d’exposition avant toute réactivation. Ses exigences restent :

- exposition comprenant achats réservés, fractions ouvertes, fractions remplies toujours détenues et soumissions de résultat incertain ;
- réservation atomique lors de l’acceptation ; transfert de la réservation vers l’exposition détenue lors du remplissage, sans double comptage ;
- libération uniquement après confirmation de l’annulation effective ou de la sortie réelle de l’exposition ;
- identifiants idempotents, rapprochement après redémarrage et refus si l’état est impossible à rapprocher ;
- distinction explicite entre ce plafond et les limites de `research/risk.py`.

Les tests de ce lot futur couvriront deux réservations de 600 € remplissant un plafond fictif de 1 200 €, le refus d’une troisième de 1 €, les validations concurrentes, les approbations rejouées, les remplissages partiels, les timeouts et les redémarrages. Aucun de ces tests ne doit émettre de mutation réelle.

**Risque.** Confondre « fermé » avec « prêt pour l’exécution ». Le registre ne suffirait d’ailleurs pas à valider une infrastructure complète de suivi et de protection des ordres.

**Dépendance.** La fermeture est immédiate. Le développement du registre ne bloque ni le monitoring en lecture seule ni les corrections de données.

**Rollback.** Rester fermé ou arrêter le daemon concerné ; aucun retour à un chemin de mutation non protégé.

### P0.3 — Supervision indépendante et code validé — A5

**Cause racine.** La supervision dépend d’une suite de tests commune et du même job que la prospection. Elle utilise aussi un `HEAD` susceptible d’avoir changé après validation.

**Architecture minimale recommandée.**

Créer un workflow dédié `monitor_positions.yml`, sans dépendance `needs` vers la prospection, DL‑V1, DL‑V2 ou l’évaluation historique.

Il disposera :

- de sa propre concurrence et de son propre timeout ;
- d’une version de code explicitement validée, identifiée par SHA ;
- des dépendances exactes utilisées lors de sa validation ;
- du dernier état privé chiffré, chargé comme donnée, indépendamment du SHA du code ;
- d’un seul processus responsable des notifications et de leur état de livraison.

La CI sera divisée en suites indépendantes : monitoring critique, intégrité des données/replays, politiques shadow. Une régression shadow ne changera pas la version validée du monitoring.

**Ordre interne du monitoring.**

1. Lire et vérifier compte, plans et carnets des positions détenues.
2. Examiner les ventes et prises de profits possibles sans attendre les enrichissements de prospection.
3. Examiner les relèvements de stop avec leurs données nécessaires.
4. Traiter les actions de gestion justifiées.
5. Seulement en leur absence, charger le module optionnel d’achat et son dernier manifeste publié.

Les imports propres aux achats doivent eux-mêmes être isolés : une erreur d’import ne doit pas empêcher l’initialisation des sorties.

Une défaillance des bougies nécessaires au trailing bloque le trailing concerné, pas une vente déjà justifiée par un stop et un carnet frais.

**Fichiers et fonctions.**

- `.github/workflows/update.yml`, `.github/workflows/ci.yml` ;
- nouveau `.github/workflows/monitor_positions.yml` ;
- `scripts/send_useful_alert.py` : séparation du chemin critique et des achats ;
- nouveau `monitoring/buy_candidates.py` ;
- `scripts/publish_data.py` : publication depuis un répertoire distinct du code exécuté ;
- `tests/test_positions.py`, nouveaux tests d’isolation du workflow.

**Tests et critère d’acceptation.**

Injecter séparément :

- un test DL en échec ;
- une erreur d’import DL ;
- une prospection en échec ou bloquée jusqu’à son timeout ;
- un journal de prospection corrompu ;
- un conflit de publication ;
- un nouveau commit arrivé pendant le cycle.

Dans tous ces cas, une sortie justifiée par des données privées valides doit rester sélectionnable et parvenir au transport SMTP simulé. Le SHA exécuté doit correspondre au SHA validé.

Les cas de compte inconnu, plan manquant ou carnet invalide doivent continuer à bloquer les décisions qui en dépendent.

**Régression / compatibilité.** Préserver les identifiants d’événements, épisodes et marqueurs de livraison existants. Éviter deux expéditeurs concurrents lors de la transition.

**Dépendance / ordre.** Après les mesures immédiates de confidentialité ; avant les expérimentations DL‑V2.

**Rollback.** Revenir au dernier SHA de monitoring validé, en conservant l’état privé courant.

Cette séparation garantit l’indépendance vis-à-vis de la prospection. Elle ne garantit pas une disponibilité absolue de GitHub, Bitvavo ou SMTP.

## P1 — À corriger avant de continuer à évaluer la Decision Layer

Les journaux peuvent continuer à être conservés pendant ces travaux. En revanche, leurs différences de performance ne devront pas être interprétées comme une validation de politique tant que les défauts de données ne sont pas isolés.

### P1.1 — Contrat temporel minimal et identités explicites

Le contrat est scindé en un noyau indispensable et une traçabilité complémentaire. La traçabilité complémentaire ne bloque pas les corrections locales A3/A4.

**P1.1a — Noyau indispensable, livré avec les correctifs qui en dépendent.**

- Une réponse consommée lie de façon cohérente le contenu, la requête et ses métadonnées. Relire une entrée globale de cache après avoir obtenu le contenu ne suffit pas si elle a été remplacée entre-temps.
- Conserver début et réception de requête, information serveur disponible et limite conservatrice d’incertitude d’horloge. Une heure HTTP n’est pas, à elle seule, un horodatage du contenu de marché.
- La clôture admissible dépend de la réponse source, jamais de l’heure ultérieure de relecture. Une donnée reçue après le cutoff de disponibilité n’est pas réintroduite dans une décision antérieure parce que sa bougie concerne une période passée.
- Chaque profil journalier a ses propres heures de tentative et d’acquisition valide ; une tentative échouée ne renouvelle aucun autre profil.
- Dès qu’une même URL peut être renouvelée dans un cycle, identifier séparément ses réponses et rattacher chaque consommation à la bonne réponse. L’ordre d’achèvement des threads ne constitue pas une identité.
- Enregistrer l’identité du scan et des entrées, leur cutoff de disponibilité et le moment où la politique a fini de produire sa décision. Les métadonnées absentes d’un ancien journal restent inconnues.

**Pourquoi le replay appartient au minimum.** `ReplayClient` construit actuellement un dictionnaire URL/paramètres où la dernière réponse l’emporte. Ajouter une collecte après clôture sans adapter cette liaison pourrait donner au replay V4 antérieur une réponse qu’il n’avait pas consommée. Cette adaptation locale est obligatoire avant d’activer ce renouvellement.

**Identités distinctes.**

| Identité | Ce qu’elle fixe |
|---|---|
| `data_policy` | Règles d’acquisition, cache, sélection et clôture des données, calcul/validation des features et traitement des absences ; version et empreinte de configuration |
| `decision_policy` | Conditions de décision, catégories, seuils et classement ; DL‑V1 conserve son identité et son comportement |
| `execution_policy` | Construction des plans, contraintes de portefeuille, sélection finale et hypothèses d’exécution |
| `evaluation_policy` | Population, événements, épisodes, labels, censure, métriques et conventions de simulation |
| `code_commit` | Révision effectivement exécutée, distincte de ces contrats fonctionnels |
| `input_snapshot_id` et références d’état | Données et passé effectivement accessibles à cette exécution |

`data_policy` remplace le nom ambigu `input_policy` dans les nouveaux manifestes. Un ancien champ peut être lu comme alias seulement si son sens est connu ; on ne lui invente pas une version corrigée.

Les faits de validité d’une donnée appartiennent au contrat de données. La décision d’utiliser cette donnée pour une surveillance ou un achat appartient au consommateur décisionnel. Modifier cette interprétation ne sera pas présenté comme une simple amélioration de collecte.

Les états et résultats dérivés sont séparés par politique de données et politique de décision. Une ancienne valeur ne doit pas écraser silencieusement la nouvelle variante dans un index commun.

**P1.1b — Complément avant la comparaison prospective.**

Compléter les liaisons nécessaires entre réponses, consommateurs, résultats et publication ; mesurer `policy_ready_at`, `published_at` et la disponibilité du chemin natif. Ajouter `release_at` pour le scénario de comparaison commune. Identifier la première disponibilité *observée par le système*, sans prétendre connaître la première disponibilité absolue chez l’exchange.

Un catalogue générique de provenance, un service de traçage distribué ou une refonte globale des formats ne sont pas requis. Toute métadonnée sans usage dans un test, un replay, une décision ou une comparaison peut attendre.

**Fichiers.** Modifications locales dans `research/http.py`, `pipeline.py`, `research/replay.py` et les lecteurs de journaux ; petit contrat partagé si cela évite une duplication, sans infrastructure nouvelle imposée.

**Acceptation.** Deux réponses différentes pour la même URL restent distinctes ; chaque consommateur rejoue la sienne ; aucune information disponible seulement après le cutoff ne traverse celui-ci ; un changement de données et un changement de politique restent séparables.

**Risque.** Sous-instrumenter permet une fuite temporelle ; sur-instrumenter retarde les correctifs et peut modifier le timing qu’on veut mesurer. Le noyau répond aux défauts démontrés et le complément est limité aux besoins du comparateur.

**Compatibilité / rollback.** Anciens formats toujours lisibles et replays historiques inchangés. Le nouveau mode peut être suspendu en refusant les données ambiguës ; aucun journal écrit n’est réécrit.

### P1.2 — Cache journalier par profil — A3

**Cause racine.** Une tentative partielle renouvelle une horloge globale, ce qui peut empêcher le rafraîchissement des autres marchés.

**Correction minimale recommandée.**

Créer un gestionnaire séparant, pour chaque marché :

- dernière tentative ;
- dernière acquisition valide ;
- état `VALID`, `STALE`, `INSUFFICIENT_HISTORY` ou `FETCH_FAILED` ;
- référence des bougies utilisées.

Une tentative échouée ou un profil vide ne doit modifier que l’état de ce marché. Elle ne renouvelle jamais les autres profils.

Pour le premier correctif, conserver les paramètres existants : renouvellement nominal de 90 minutes et limite de fraîcheur de trois heures. Leur optimisation n’appartient pas à ce lot.

**Préservation de V4.** Ne pas modifier les sources archivées. Un adaptateur d’acquisition fournira les profils au moteur figé ; la politique d’entrée corrigée sera identifiée séparément. Le mode de replay historique gardera ses entrées et son ancien état.

**Fichiers et fonctions.** Nouveaux `research/trend_cache.py` et `research/v4_adapter.py` ; orchestration dans `pipeline.py`. Réutiliser la fonction de calcul de profil sans modifier sa formule.

**Tests et critère d’acceptation.**

- Reproduction AAA + nouveau marché sans historique suffisant.
- Le profil AAA est renouvelé à son échéance malgré les échecs répétés du nouveau marché.
- Échec, reprise, expiration exacte et redémarrage.
- Un profil vieux de plus de trois heures ne fournit pas silencieusement une preuve structurelle valide à DL‑V2.
- Sur les mêmes bougies et le même état, le calcul V4 reste identique.
- Les dépendances d’un score, notamment les références BTC/ETH de force relative, ont une fraîcheur vérifiable ; un profil local récent ne rend pas automatiquement ses dépendances fraîches.

**Régression / compatibilité.** Risques : hausse des appels API, migration donnant artificiellement un âge nul, modification non déclarée des inputs V4. Les anciens profils ne sont utilisables comme amorçage que si leur fraîcheur est vérifiable.

**Dépendance / ordre.** Après le seul noyau temporel nécessaire à A3, éventuellement dans le même lot ; avant le classement V2. La traçabilité enrichie ne bloque pas ce correctif.

**Rollback.** Suspendre l’utilisation des profils corrigés ou des catégories dépendantes. Ne pas réactiver leur acceptation silencieuse lorsqu’ils sont périmés.

### P1.3 — Clôture effective des bougies et cache 15 minutes — A4

**Cause racine.** Une réponse collectée pendant une bougie ouverte est réinterprétée avec une heure ultérieure.

**Correction minimale recommandée.**

- Décider de la clôture à partir de l’instantané réellement collecté, jamais de l’heure de relecture du cache.
- En l’absence d’un horodatage du contenu de marché exploitable, utiliser conservativement le début de requête corrigé de l’incertitude d’horloge. L’en-tête HTTP `Date` ne garantit pas à lui seul la clôture du contenu.
- Si la dernière clôture requise a été franchie après cette collecte, renouveler la réponse ou déclarer cette clôture indisponible.
- Renvoyer contenu et métadonnées comme une unité cohérente.

Une requête commencée avant clôture et reçue après clôture ne fournit pas automatiquement une preuve que les valeurs sont définitives.

**Fichiers et fonctions.** `research/http.py` : acquisition/cache/replay ; `research/features.py` : validation des bougies closes ; `pipeline.py::collect_universe` ; `scripts/send_useful_alert.py::market_inputs`.

**Tests et critère d’acceptation.**

- Collecte dix secondes avant clôture, relecture dix secondes après.
- Requête traversant elle-même la clôture.
- Même URL appelée deux fois avec deux OHLC différents.
- Décalage d’horloge, réponse tardive, cache ancien.
- **Aucune bougie encore ouverte dans l’instantané source n’est déclarée close.**
- Le replay conserve la bonne réponse pour chaque phase.

**Régression / compatibilité.** Une correction conservatrice peut retirer temporairement une feature jusqu’au rafraîchissement. C’est une indisponibilité explicite, pas une erreur à compenser par des données inventées.

Les bougies en formation utilisées par le mode historique V4 restent identifiées comme telles ; leur consommation historique ne sera pas réécrite.

**Dépendance / ordre.** Avec le noyau P1.1a et les tests de liaison des réponses du replay ; avant les nouvelles mesures. Aucune attente d’un système général de traçabilité.

**Rollback.** Refuser les réponses ambiguës. Ne pas revenir à leur validation avec l’heure courante.

### P1.4 — Nouvelle taxonomie de qualité

Remplacer le booléen global comme source unique de décision par **des capacités justifiées par leurs données**.

Chaque observation indiquera notamment si elle permet :

- d’interpréter la structure ;
- de mesurer l’entrée ;
- de proposer une exécution immédiate ;
- de construire un plan passif ;
- de suivre un repli ;
- d’évaluer ultérieurement le résultat.

Ces capacités peuvent différer pour un même marché.

| Situation | Traitement recommandé |
|---|---|
| Identité de marché incohérente, horloge inexploitable, valeurs contradictoires contaminant toutes les preuves nécessaires | Veto sur la décision actuelle ; conservation du diagnostic |
| Structure vérifiée comme invalidée | Invalidation du setup courant ; une nouvelle structure devra être observée |
| Données suffisantes pour la structure, insuffisantes pour l’entrée | Surveillance possible ; aucun achat immédiat |
| Enrichissement secondaire absent | Information limitée, sans pénalité numérique automatique ni score inventé |
| Bougies absentes faute de transactions, absence effectivement documentée | Conserver l’absence ; invalider seulement les calculs nécessitant une continuité non disponible |
| Trou de données de cause inconnue | `GAP_UNKNOWN` ; ne pas le rebaptiser absence de transactions |
| Spread/liquidité incompatibles avec une proposition d’ordre | Bloquer l’activation de l’ordre ; conserver éventuellement le candidat ou son plan inactif |
| Profil journalier périmé | Structure dépendante à revalider ; interdiction de classer comme valide un score périmé |
| Rejets de prix ou mèches préoccupants | Interprétation selon les raisons et l’état du setup ; pas de veto fondé sur le seul nom du statut |

Bitvavo confirme que les intervalles sans transaction peuvent ne produire aucune bougie. Cela justifie de distinguer absence légitime et défaut de collecte, sans conclure automatiquement laquelle explique un trou donné. [Documentation Bitvavo](https://docs.bitvavo.com/docs/rest-api/get-candlestick-data/)

**Correspondance des flags.**

- `INVALID_5M`, `INVALID_15M`, `MISSING_*` : examiner la cause et les facteurs affectés. Aucun veto global par simple préfixe.
- `ENTRY_INPUTS_UNAVAILABLE`, `NOT_ENTRY_ENRICHED` : entrée inconnue ; surveillance seulement si les scores structurels reposent sur des données indépendamment valides.
- `WIDE_SPREAD`, `WIDE_SPREAD_RISK`, `LOW_LIQUIDITY`, `ILLIQUID` : contraintes d’exécution explicites, conservées pour l’activation d’un achat.
- `STALE_DAILY_PROFILE` : bloque l’utilisation actuelle du profil concerné.
- `PIPELINE_DEGRADED` : décrire les composants indisponibles plutôt que supposer que chaque marché est également atteint.
- `DANGEROUS_STRUCTURE` : décomposer ses raisons avant de décider de sa portée.

Un candidat conservé avec un plan inactif ne doit jamais être présenté comme un ordre à placer.

**Fichiers.** Nouveau `research/quality.py`, `research/features.py`, `pipeline.py`, `research/input_contract.py`, puis consommateur V2.

**Tests / acceptation.**

- Modifier une feature secondaire sans toucher aux preuves structurelles ne supprime pas le candidat.
- Une donnée indispensable invalide ne devient pas exploitable par renormalisation ou valeur par défaut.
- Chaque capacité est accompagnée de ses raisons et références de données.
- La couverture est publiée par capacité et par catégorie.
- Le taux d’admissibilité n’est pas une cible à maximiser : le critère est la validité des distinctions et leur utilité prospective.

**Compatibilité / rollback.** Conserver les flags bruts et l’ancienne vue pour DL‑V1. Ajouter la nouvelle interprétation dans un espace versionné. Désactiver ce consommateur suffit au rollback.

### P1.5 — Contrat de spread — A6

**Cause racine.** Les noms produits et consommés ne correspondent pas, ce qui rompt la progression de sévérité.

**Correction minimale.** Construire un diagnostic canonique du spread à partir du flag brut et, lorsqu’elle est disponible, de sa valeur numérique. La sévérité doit être ordonnée. Les règles d’activation des achats utiliseront ce diagnostic.

DL‑V1 restera inchangée comme référence. La correction de classement sera appliquée dans DL‑V2, sans prétendre avoir « corrigé V1 » tout en conservant exactement son comportement.

**Fichiers.** `research/quality.py`, `research/decision_layer_v2.py`, `monitoring/buy_candidates.py`. `v4_detector.py` reste le producteur de référence.

**Tests / acceptation.**

- Rejouer le couple `WIDE_SPREAD_RISK` / `WIDE_SPREAD`.
- À autres informations constantes, aggraver le spread ne retire jamais une contrainte d’exécution.
- Un candidat peut rester surveillé tout en étant interdit de proposition d’achat.
- Aucune normalisation ne modifie rétrospectivement les payloads V1.

**Régression / compatibilité.** Risque principal : réintroduire un veto global et supprimer inutilement des candidats latents. Préserver les deux représentations, brute et interprétée.

**Dépendance / ordre / rollback.** Après la taxonomie ; avant V2 et l’activation d’alertes. Rollback vers absence de nouvelle proposition, pas vers le contournement du contrôle.

### P1.6 — Contrat des mèches — A7

**Cause racine.** Le consommateur attend un booléen absent. De plus, le statut `DANGEROUS_STRUCTURE` mélange actuellement spread, liquidité et rejets de prix.

**Correction minimale.**

- Lire les statuts et raisons réellement produits.
- Séparer raisons d’exécution et raisons de structure de prix.
- Abandonner dans V2 la pénalité numérique implicite fondée sur un booléen inexistant.
- Traiter les mèches comme une condition de confirmation ou d’invalidation documentée, selon leur nature.

`POTENTIALLY_EXPLOITABLE` ne signifie ni « achat » ni « danger ». `UNAVAILABLE` ne signifie pas `NORMAL`.

**Fichiers.** `research/features.py::wick_setup`, `research/quality.py`, `research/decision_layer_v2.py` ; tests de contrat utilisant les vrais payloads.

**Tests / acceptation.**

- Couvrir les cinq statuts réels.
- Comparer `DANGEROUS_STRUCTURE` dû seulement au spread à celui dû aux rejets de prix.
- Vérifier qu’aucune branche V2 ne dépend de `is_wick_setup`.
- Chaque changement de disponibilité ou de structure produit une explication cohérente, sans pénalité arbitraire supplémentaire.

**Régression / compatibilité.** Préserver le payload historique et le replay V1. Le nouveau diagnostic est versionné ; sa désactivation permet le rollback V2.

**Dépendance / ordre.** Après la taxonomie ; application décisionnelle lors du lot V2.

### P1.7 — Sélection des alertes avec fallback — A8

**Cause racine.** La réduction à un candidat intervient avant les contrôles privés.

**Ordre recommandé :**

**détection → liste classée → contrôles d’éligibilité → sélection finale unique → contrôle final de fraîcheur → notification.**

Concrètement :

1. Produire la liste ordonnée des candidats dont l’épisode est encore éligible.
2. Vérifier d’abord les conditions globales : compte connu, budget connu, absence d’action de gestion prioritaire.
3. Examiner les candidats dans cet ordre.
4. Un rejet propre à AA permet d’examiner BB.
5. Un défaut global, comme un compte périmé, bloque tous les achats.
6. Conserver au maximum le premier candidat réellement admissible.
7. Juste avant notification, revérifier les données susceptibles d’avoir vieilli.
8. Marquer uniquement la proposition effectivement délivrée après succès SMTP.

Le fallback doit parcourir le classement publié. Il ne doit ni rechercher rétrospectivement un meilleur gagnant ni déclencher un enrichissement massif sans budget de temps.

**Fichiers et fonctions.** `email_alert_v4.py::select_events` : extraire une fonction retournant la liste complète tout en conservant l’interface historique ; `monitoring/buy_candidates.py` ; `scripts/send_useful_alert.py`.

**Tests / acceptation.**

- AA meilleur mais dérive de prix excessive ; BB admissible : **BB seul**.
- AA déjà détenu ; BB admissible : BB seul.
- AA refusé pour corrélation ; BB admissible : BB seul.
- AA et BB admissibles : AA seul.
- Tous refusés : aucune proposition.
- Compte inconnu : aucune proposition, sans parcours inutile.
- Vente prioritaire : aucun achat.
- Échec SMTP : aucun faux marqueur de livraison.
- Dans tous les cas : **nombre de nouvelles propositions d’achat ≤ 1**.

**Régression / compatibilité.** Le risque majeur serait de retirer `[:1]` et d’envoyer ensuite plusieurs achats. La sélection unique doit être un invariant explicite du nouveau chemin.

**Dépendance / ordre.** Après l’isolation du monitoring et le contrat d’éligibilité.

**Rollback.** Désactiver les nouveaux achats tout en conservant la supervision des positions et son état de livraison.

### P1.8 — Continuité de l’événement historique — A9

**Cause racine.** La continuité ne couvre pas la dernière liaison vers la bougie de franchissement.

**Correction minimale.** Vérifier toute la séquence, jusqu’à la bougie déclenchante, et la durée réelle représentée. Un trou non résolu doit produire un état d’observation insuffisante, pas un événement court confirmé.

**Fichier / fonction.** `research/evaluation.py::market_control`, avec version explicite du diagnostic historique.

**Tests / acceptation.**

- Douze bougies, trou de 3 h 50, puis franchissement : aucun événement court confirmé.
- Séquence continue équivalente : événement reconnu.
- Doublon contradictoire, ordre inversé, bougie partielle et limite exacte de fenêtre.
- Aucun délai de détection ni faux négatif n’est attribué à partir d’un événement insuffisamment observable.

**Régression / compatibilité.** Certains diagnostics anciens vont disparaître dans la nouvelle mesure. Les anciens rapports restent consultables ; les résultats recalculés portent une nouvelle version d’évaluation.

**Dépendance / ordre / rollback.** Après le contrat temporel ; avant les comparaisons. Rollback vers le rapport ancien explicitement étiqueté, sans mélanger les métriques.

### P1.9 — Contrôles courant et historique explicites — A10

**Cause racine.** Deux diagnostics différents sont présentés sous un intitulé ambigu.

**Correction minimale.**

- Exposer séparément `market_control_current` et `market_control_history`.
- Le premier décrit la présence dans les listes publiées au moment considéré.
- Le second utilise le journal complet et la chronologie corrigée.
- Conserver provisoirement les anciens fichiers comme interface de compatibilité, avec une portée explicite.
- Corriger les libellés publics : « absent de la liste courante publiée » ne signifie pas « jamais détecté ».

**Fichiers.** `pipeline.py` : génération et `report_text` ; `scripts/publish_data.py` ; préparation Pages dans le workflow ; `README.md`, `docs/EVALUATION.md`.

**Tests / acceptation.**

- Un marché absent du top courant mais détecté précédemment doit être correctement décrit dans les deux sorties.
- Le contrôle historique ne dépend pas des plafonds de 50/40 lignes.
- Les pages, fichiers et métadonnées identifient sans ambiguïté leur portée et leur version.

**Régression / compatibilité.** Risque de casser les lecteurs des anciens noms. Préserver les alias, sans préserver leur ambiguïté documentaire.

**Dépendance / ordre / rollback.** Après A9 ; rollback des nouveaux points d’accès possible, avec maintien de l’explication de portée.

## P2 — Nouvelle politique Decision Layer candidate

### P2.1 — Organisation générale

Créer `research/decision_layer_v2.py`, avec une politique distincte, par exemple `DECISION_LAYER_V2_CANDIDATE`.

Le traitement sera :

1. Vérifier la provenance et la validité des informations utilisées.
2. Distinguer structure valide, structure invalidée et structure non vérifiable.
3. Déterminer l’état d’entrée : mesuré favorable, mesuré défavorable ou inconnu.
4. Déterminer les catégories compatibles.
5. Classer les candidats comparables.
6. Produire séparément catégorie, état de préparation, contraintes et action permise.

**Être dans une catégorie ne constitue pas une autorisation de proposer un achat.**

Conserver `research/decision_layer.py` et les journaux V1. Les sorties V2 iront dans des fichiers et journaux distincts. Le runner devra recevoir un `scan_id` explicite ; il ne devra pas choisir silencieusement « le dernier fichier » après une publication concurrente.

### P2.2 — Opportunity seul : baseline expérimentale, sans optimalité présumée

La première candidate V2 utilise Opportunity décroissant, avec départage déterministe par marché. Elle porte une identité expérimentale explicite, par exemple `DL_V2_OPPORTUNITY_BASELINE_SHADOW`.

L’objectif est de retirer les termes additionnels dont la contribution marginale n’est pas établie. Ce choix n’affirme ni que toutes les dépendances entre facteurs sont nuisibles, ni que le classement obtenu est optimal.

Dans le code actuel, Opportunity est le maximum de deux chemins contenant respectivement 23 % et 68 % de Trend. Opportunity seul n’est donc ni un facteur pur ni une garantie d’absence de corrélation.

| Information | Traitement de la baseline |
|---|---|
| Opportunity | Classement principal conservé |
| Trend | Condition structurelle et diagnostic, sans nouveau terme additif au rang |
| Entry | État de préparation et catégorie, inconnu si non mesuré |
| Récurrence | Suivi des épisodes et stabilité, sans bonus numérique |
| Hausse 24 h / chase | Diagnostic et contraintes d’entrée, sans double pénalité additionnelle |
| Mèches | Statuts et raisons explicites, sans pénalité implicite |
| Carnet, coûts, portefeuille et plan | Contraintes d’exécution séparées du classement |

**Seuils conservés comme paramètres expérimentaux.** 7,40 / 7,30 / 6,80 / 5,80 / 7,60. Leur conservation isole mieux les changements ; elle ne leur confère pas de validation scientifique.

Comparer V2 complète à V1 complète mesure l’effet du paquet de décisions : qualité, catégories et classement. Si l’on veut attribuer spécifiquement un gain à Opportunity seul, une ablation devra maintenir les mêmes données, catégories et candidats admissibles, et ne changer que le classement. Cette attribution n’est pas autorisée par la seule comparaison globale.

Aucune recherche immédiate de nouveaux poids ou d’un classement multifactoriel n’est ajoutée au chemin critique. Une hypothèse ultérieure sera versionnée et évaluée sur des données nouvelles.

### P2.3 — Traitement du cas IOST

Conserver la valeur historique `entry_score=4.5` dans le payload V4, mais exposer dans la nouvelle interprétation :

- `entry_status=UNKNOWN` ;
- `entry_score_measured=null` ;
- la cause `NOT_ENTRY_ENRICHED`.

Puis appliquer deux cas :

1. **Opportunity/Trend valides et suffisamment frais**, indépendamment du défaut d’entrée : candidat latent possible, avec enrichissement requis avant toute promotion.
2. **Les défauts 5m/15m ou la fraîcheur rendent aussi la structure non vérifiable** : observation conservée en attente de revalidation, sans classement latent présenté comme fiable.

Le véritable IOST historique ne sera donc pas automatiquement « sauvé ». Son résultat dépendra des preuves disponibles à cet instant, pas de son mouvement ultérieur.

**Acceptation.** Le cas synthétique complet reste distinct du cas réel incomplet. Aucun achat immédiat ne peut provenir d’une valeur d’entrée par défaut.

### P2.4 — Catégories conservées ; nouvelles heuristiques exclusivement expérimentales

Les quatre lectures sont conservées. Le re-entry décrit une phase du setup ; la limite passive décrit un mode d’entrée. Ces dimensions restent séparées dans la donnée, même si l’affichage choisit une catégorie principale.

**Règle commune de cette phase 3 :** toutes les sorties DL‑V2 sont shadow. Aucune catégorie, aucun prix expérimental et aucune confirmation de reprise ne sont routés vers les achats actifs, les notifications d’achat ou un exécuteur.

| Lecture | Preuves nécessaires | Résultat de cette phase |
|---|---|---|
| Immédiat | `buy_ready` V4, Entry mesurée, preuves fraîches, contraintes explicites | Éligibilité théorique journalisée ; aucune activation V2 |
| Passive | Structure forte et valide, niveau d’entrée et invalidation explicitement justifiables | Candidat ou plan hypothétique inactif ; absence de niveau = absence de plan |
| Latente | Structure forte vérifiable, sans entrée immédiatement justifiée | Surveillance et besoin de revalidation/enrichissement |
| Pullback / re-entry | Repli chronologique observable, référence et invalidation enregistrées | État de setup ; confirmation éventuelle enregistrée comme hypothèse |

**Corrections de cohérence conservées.**

- Entry 6,80 cesse d’être une borne supérieure faisant disparaître un candidat de la lecture passive ; une amélioration d’Entry seule ne supprime pas son admissibilité à la surveillance.
- Une structure forte et valide sans entrée justifiée reste latente. Une structure non vérifiable reste en attente de revalidation.
- Le re-entry ne contourne pas la condition de structure forte.
- Une simple variation 24 h négative ne prouve pas un pullback.
- Le signal `entry_mode=PULLBACK` effectivement calculé peut servir de preuve existante à examiner ; il ne valide pas à lui seul une nouvelle règle de reprise rentable.
- `TOO_LATE` bloque l’entrée immédiate tant que la contrainte est actuelle. Une nouvelle observation, et non le replay du même snapshot, est nécessaire pour réexaminer cette contrainte.

**Deux hypothèses optionnelles à tester séparément.**

1. **Prix passif au support observé.** Le support calculé dans `research/features.py` est un niveau descriptif. S’il est utilisé pour une expérience, enregistrer avant tout remplissage simulé son heure, ses bougies sources, le prix arrondi au tick, l’invalidation, l’expiration et les coûts. Le niveau doit être strictement sous l’ask et permettre un plan de risque valide. Ni un prix plausible ni le contact d’une mèche ne prouvent un remplissage réalisable.
2. **Reprise au-dessus du plus haut de la bougie de repli précédente.** Enregistrer ex ante la référence haute, le début du repli et l’invalidation. Les données closes peuvent déclencher un événement expérimental de confirmation ; elles ne déclenchent aucune proposition active nouvelle.

Chaque hypothèse reçoit son propre identifiant et reste désactivable indépendamment de la baseline Opportunity. On peut différer leur instrumentation si elle retarde les corrections démontrées ou si les données nécessaires ne sont pas observables. Un test historique d’IOST ne suffit pas à les valider.

**Contrat de plan.** Si la simulation de prix passif est implémentée, elle reçoit un prix d’entrée envisagé distinct du carnet observé. Ne jamais falsifier l’ask pour réutiliser `research/risk.py::plan`. L’appel historique sans prix expérimental doit conserver son comportement.

**Acceptation spécifique.** Aucun événement issu de ces deux hypothèses n’atteint les fichiers d’achat actifs, le sélectionneur d’alertes d’achat ou une mutation privée. Les plans simulés sont datés avant leur issue et leurs ambiguïtés restent visibles.

**Promotion ultérieure.** Nécessite une validation prospective propre et une décision de promotion distincte. La réussite technique de la baseline V2 ne promeut pas automatiquement ses expériences optionnelles.

### P2.5 — Tests, acceptation et rollback de V2

**Fichiers.** `research/decision_layer_v2.py`, `research/quality.py`, runner versionné, nouveau `tests/test_decision_layer_v2.py`. L’adaptation de `research/risk.py` pour un prix d’entrée explicite appartient uniquement au lot expérimental passif, s’il est retenu.

**Tests nécessaires.**

- Cas IOST réel et synthétique.
- Frontières 5,80 et 6,80, avec les mêmes autres informations.
- Amélioration d’Entry ne supprimant pas un candidat jusque-là admissible.
- Variation 24 h négative ne suffisant pas à créer un re-entry.
- Spread aggravé ne facilitant pas une proposition d’ordre.
- Tous les statuts de mèches.
- Données manquantes conservées comme inconnues.
- Snapshot répété ne créant ni nouvelle confirmation ni nouvel épisode.
- Ordre des marchés d’entrée sans effet sur les résultats.
- Replay déterministe, sans accès réseau de secours.
- Aucune route des hypothèses support/reprise vers les achats actifs ; désactivation de ces hypothèses sans modifier la baseline ni les sorties de positions.

**Critère d’acceptation technique.** Les invariants sont respectés sur fixtures et replays ; chaque classement, abstention et promotion est explicable par les données enregistrées. Ce critère ne constitue pas une preuve de performance.

**Régression / compatibilité.** La couverture des catégories et leurs rangs vont changer : c’est précisément la nouvelle politique évaluée. V4 et V1 restent rejouables et leurs journaux ne sont pas modifiés.

**Rollback.** Désactiver le runner V2 et conserver ses journaux. V1 reste une baseline shadow disponible ; les correctifs de confidentialité, d’horodatage et de supervision ne sont pas annulés avec V2.

## P3 — Protocole statistique de validation

### P3.1 — Deux comparaisons et une attribution explicite aux données

**Comparaison à cutoff commun : qualité à information équivalente.**

1. Fixer l’univers EUR actif et un cutoff de disponibilité.
2. Construire un snapshot immuable des informations effectivement disponibles avant ce cutoff.
3. Fournir ces informations et le même passé accessible à V4, DL‑V1 et DL‑V2, avec `data_policy` identique. Chaque politique conserve son propre état algorithmique déterministe ; on ne force pas leurs mémoires internes à devenir identiques.
4. Comparer les décisions et le rappel à budget commun sur les mêmes événements. Une information récupérée plus tard ne peut entrer dans cette comparaison.
5. Pour une simulation d’exécution commune, fixer avant le test une règle de disponibilité commune et une échéance maximale. Un résultat non disponible à l’échéance est déclaré indisponible ; il ne fait pas attendre indéfiniment les autres.

Cette disponibilité commune est une convention analytique. Elle ne retarde pas les chemins de production.

**Comparaison native end-to-end : résultat effectivement accessible à temps.**

- Mesurer séparément déclenchement, collecte, enrichissement, disponibilité du score, publication, consommation par le monitoring et disponibilité de l’alerte justifiée.
- Une politique utilise seulement ce qui lui était réellement accessible à son heure native. V4 ne reçoit pas le retard de DL‑V2 ; DL‑V2 ne reçoit pas rétrospectivement l’heure de V4.
- Inclure les cycles manqués, erreurs, données périmées et publications en échec dans le bilan opérationnel.
- Mesurer délai utile, détections manquées, propositions encore admissibles et, lorsque les plans et données le permettent, résultats économiques simulés. Un histogramme de durées seul ne suffit pas.
- Garder une référence d’événement commune pour comparer le rappel. Déplacer le début du mouvement avec l’heure de chaque politique masquerait précisément le coût du retard. La simulation d’entrée, elle, commence à la disponibilité propre du plan considéré.

Le temps de calcul d’un replay effectué aujourd’hui ne reconstitue pas une ancienne latence native. Des étapes historiques non horodatées restent inconnues. En shadow, l’acceptation simulée par un transport ne sera pas présentée comme un email réel reçu.

**Attribution aux données et à la politique.**

| Contraste | Question mesurée | Conditions |
|---|---|---|
| Même politique, `data_policy` historique versus corrigée | Effet des entrées corrigées | Même période, mêmes événements et même évaluation ; deux jeux d’entrées réellement disponibles ou reconstructibles sans données inventées |
| V4 versus DL‑V1 versus DL‑V2, `data_policy` corrigée commune | Effet des politiques de décision | Même cutoff, même population, budget commun et états initialisés de façon documentée |
| Versions natives complètes | Résultat du système avec sa latence et ses indisponibilités | Temps et étapes réellement observés, scénarios identifiés |

Les contrastes minimaux de données concernent V4 et/ou V1 à politique inchangée. Il n’est pas nécessaire de construire toutes les cases d’un grand plan factoriel si leurs données manquent. Une case non reconstructible est déclarée indisponible. Les anciennes données ambiguës restent confinées à la référence expérimentale.

Un gain total n’est pas automatiquement la somme d’un gain « données » et d’un gain « DL » : leurs interactions peuvent compter. Une comparaison entre deux dates et deux politiques différentes ne démontre aucun de ces effets séparément.

**Exécution économique.** Conserver les mêmes règles de risque et des portefeuilles théoriques séparés par scénario. Une réservation de V4 ne doit pas consommer le budget de la branche DL‑V2. Les variantes support/reprise sont des scénarios expérimentaux identifiés, pas des modifications silencieuses du scénario principal.

### P3.2 — Population, événements et épisodes

**Population.** Tous les marchés EUR actifs du snapshot, y compris les marchés non analysés par V4. « Non analysé » doit rester distinct de « analysé sans signal ».

**Critère principal conservé.** +5 % en quatre heures avec excursion adverse avant cible limitée selon le protocole existant. Les autres horizons restent secondaires ; aucun choix après résultats.

**Deux unités complémentaires.**

- Opportunités/événements : pour mesurer détection, rappel et délai.
- Propositions et épisodes : pour mesurer sélection, répétition et exécutabilité.

Les épisodes seront identifiés sans information future : même marché, même setup, mêmes niveaux structurants. Un nouveau scan n’est pas un nouvel essai. Une sortie d’état temporaire due à une donnée manquante ne suffit pas à créer un nouvel épisode.

La séparation actuelle de quatre heures reste un repère descriptif ; elle ne sera pas assimilée à une indépendance statistique.

### P3.3 — Censure conservée et faux négatifs séparés

Distinguer horizon immature, futur manquant, absence de transactions documentée, défaut de collecte, ambiguïté OHLC et impossibilité de documenter une exécution.

**Aucune donnée future manquante ne devient un FP ou un TN.** Une absence de signal avec un résultat positif observable peut être un FN, y compris si le système s’est abstenu pour qualité.

Publier la censure par marché, liquidité, catégorie et politique, la part de population effectivement mesurée, ainsi que des bornes pessimistes/optimistes lorsque le résultat est partiellement identifiable. Si la conclusion change selon le traitement admissible des cas inconnus, elle reste indéterminée. Les marchés difficiles ne sortent pas du dénominateur de population.

**Deux métriques de faux négatifs, à unité et fenêtre identiques.**

Soit `Y` un événement positif observable, `G` l’existence de données suffisantes au moment pertinent, `D_policy` la sélection utile produite par la politique et `D_system` sa disponibilité effective au stade opérationnel mesuré, par exemple la publication. Ces deux décisions sont reliées au même événement, au même budget et à la même fenêtre utile.

- **Faux négatifs end-to-end :** événements `Y` sans `D_system`, y compris lorsque `G` est faux, qu’un enrichissement manque ou qu’un cycle échoue. Taux = ces FN / tous les événements positifs observables de la population déclarée.
- **Faux négatifs décisionnels conditionnels :** événements `Y` avec `G` et sans `D_policy`. Taux = ces FN / événements positifs observables avec `G`.

Une sélection correcte perdue lors de la publication n’est donc pas un faux négatif du classement. Elle reste un faux négatif end-to-end, attribué au chemin d’intégration. Une politique qui échoue malgré des données disponibles conserve une abstention technique explicite ; elle n’est pas discrètement retirée de son dénominateur ni décrite comme un rejet heuristique.

`G` est défini avant les résultats, par les preuves nécessaires à l’usage considéré. Il ne dépend ni du rang obtenu, ni d’un seuil de score, ni de l’issue future. Le booléen global actuel `data_quality.ok` ne devient pas automatiquement ce masque.

Pour comparer des politiques, publier d’abord le sous-ensemble exploitable commun. Les diagnostics utilisant des exigences propres à chaque politique sont également utiles, mais leurs dénominateurs différents empêchent une comparaison directe de leurs seuls taux.

**Pas de double comptage ni de causalité inventée.**

- Les FN conditionnels appartiennent au bilan end-to-end du même chemin ; leurs totaux ne s’additionnent pas.
- Décomposer les FN end-to-end en groupes exclusifs : données insuffisantes ; données exploitables mais aucune sélection utile de la politique ; sélection utile produite mais perdue ou trop tardive dans l’intégration.
- Plusieurs flags peuvent être conservés comme diagnostics, sans être additionnés comme autant d’opportunités manquées.
- Un défaut de données concomitant à un FN ne prouve pas que réparer ce défaut aurait produit une détection. Cette affirmation demande un contre-factuel identifiable.
- Distinguer les étapes « détecté », « classé dans le budget », « publié », « proposition d’achat admissible » et « notification ». Une hausse ultérieure ne rend pas automatiquement injustifié un blocage légitime de portefeuille.

Les périodes sans scan doivent rester visibles via une chronologie de référence et des résultats de marché observables indépendamment des signaux. Si ces résultats manquent aussi, le coût en FN de ces périodes demeure inconnu et fait partie de la censure, pas d’un bilan déclaré sans échec.

### P3.4 — Détection, classement et catégories

Mesurer séparément :

| Dimension | Mesures |
|---|---|
| Détection | TP, FP, FN, rappel, précision, délai avant mouvement |
| Classement | Rappel dans les trois premiers candidats, rang du premier candidat pertinent |
| Catégories | Couverture, résultats et transitions propres à chaque bucket |
| Stabilité | Temps de présence, changements de rang, rotation du top, répétitions sans information nouvelle |
| Qualité et intégration | FN end-to-end, FN conditionnels, couverture de chaque dénominateur, causes d’abstention et étapes manquantes |
| Trajectoire | MFE, MAE, temps jusqu’à cible/invalidation |

Le budget commun de trois candidats reprend le `top_n=3` existant. Les listes natives complètes seront également conservées.

V4 ne possède pas exactement les quatre catégories V1/V2. Une correspondance descriptive peut être publiée, mais elle ne devra pas lui attribuer une décision qu’elle n’a jamais produite.

### P3.5 — Exécution, frais et résultats économiques

Un classement latent n’est pas un trade. Un re-entry en attente ne reçoit pas le rendement d’un achat supposé au premier signal.

Une simulation économique nécessite un plan enregistré **avant** son éventuel remplissage :

- heure de disponibilité ;
- type et prix d’entrée ;
- quantité ;
- stop et cible ;
- durée de validité ;
- hypothèses de frais et slippage ;
- données permettant de juger l’exécution.

Pour la comparaison, utiliser les mêmes règles de construction de plan, les mêmes limites de capital et au maximum une nouvelle proposition d’achat par cycle. Les paramètres actuels de risque restent inchangés.

**Conventions conservatrices à conserver.**

- Pas de remplissage certain déduit du seul passage d’une mèche sous une limite.
- Pas de crédit de TP lorsque l’ordre entrée/cible dans la même bougie est indéterminé.
- Gap à travers le stop pris en compte.
- Absence de données d’exécution explicitement censurée ou bornée.
- Frais et slippage appliqués de manière identique aux trois politiques.
- Hypothèses de coûts distinguées des frais réellement vérifiés.

Une analyse de sensibilité sera définie avant le test, notamment sur les coûts et sur un retard d’action. Elle ne remplacera pas la mesure de latence effective.

La lecture économique inclura aussi les propositions non remplies et le capital immobilisé. Comparer uniquement la moyenne des trades remplis serait insuffisant.

### P3.6 — Pilote technique, dimensionnement justifié, puis held-out neuf

**Séquence obligatoire.**

1. L’historique déjà examiné sert au développement, aux replays et aux reproductions de bugs.
2. Une phase prospective technique vérifie les données, les épisodes, les horodatages, les branches et les mesures. Ses résultats restent du développement.
3. Estimer pendant cette phase les quantités nécessaires au dimensionnement : fréquence des épisodes utiles, fréquence des paires discordantes entre politiques, taux de labels observables, dispersion des différences appariées et dépendances temporelles/intermarchés.
4. Définir et justifier, avant le held-out, la métrique et le contraste principaux, la taille d’effet jugée utile, la précision ou puissance recherchée, le risque d’erreur accepté, le traitement des comparaisons multiples et la règle de durée/analyse.
5. Geler code, `data_policy`, politiques de décision/exécution/évaluation, états d’amorçage et hypothèses ; ouvrir ensuite une période nouvelle.
6. Purger les labels de développement chevauchant la validation et appliquer un embargo au moins égal au plus long horizon évalué. Les états roulants peuvent utiliser le passé effectivement disponible, jamais les labels futurs.

**Arbitrage sur 5 %, 80 % et cinq points de rappel.** Ces valeurs ne sont plus des critères obligatoires du plan final. Elles peuvent figurer comme scénarios de dimensionnement comparables, sans privilège scientifique particulier.

Le pilote renseigne la variance, la disponibilité des labels et les dépendances. Il ne choisit pas mécaniquement le niveau d’erreur acceptable, la puissance souhaitable ou l’amélioration qui aurait une utilité opérationnelle. En particulier, on ne dimensionne pas le held-out sur le gain le plus favorable observé pendant la mise au point.

Le dimensionnement se fera sur des différences appariées et des blocs temporels regroupant les marchés, avec une sensibilité aux longueurs de blocs et à l’incertitude du pilote. Il n’utilisera ni le nombre brut de scans ni une hypothèse automatique d’indépendance des épisodes. Le contraste principal et les lectures secondaires seront préenregistrés pour éviter de sélectionner après coup une métrique ou un adversaire favorable.

**Durée.** Conserver trente journées nouvelles comme plancher calendaire de validation, hérité du plan de phase 2. Ce plancher ne garantit ni puissance, ni diversité suffisante des régimes, ni disparition de la censure. La durée planifiée peut être supérieure selon le pilote ; si la précision requise est inaccessible, conclure que les données ne permettent pas la validation annoncée.

La date d’analyse ou la règle d’arrêt est fixée avant consultation du held-out. Une prolongation repose uniquement sur une règle préétablie de disponibilité/information, sans arrêt au premier résultat favorable. Les nouveaux résultats ne servent pas à réajuster les poids, les seuils ou les critères d’acceptation.

**Après changement.** Toute modification substantielle de données, décision ou hypothèse de simulation après consultation du held-out crée une nouvelle version et impose une nouvelle validation. Les données déjà consultées rejoignent le développement.

**Risque / rollback.** Un pilote court peut sous-estimer la dépendance ou surestimer la couverture. Utiliser des scénarios prudents ; si l’analyse est fragile ou insuffisamment informative, maintenir le shadow et conserver les journaux. Aucun rattrapage par sélection de fenêtres favorables.

### P3.7 — Critères de passage

| Décision | Conditions minimales |
|---|---|
| **Corriger un bug technique** | Reproduction du défaut, test échouant avant et passant après, invariants préservés, changement versionné |
| **Modifier une règle de décision** | Problème identifié, hypothèse explicite, nouvelle candidate, protocole fixé avant validation ; aucune modification silencieuse de V1 |
| **Déclarer une amélioration de détection** | Contraste et métrique préenregistrés à budget commun ; intervalle apparié excluant zéro dans le sens du gain, au niveau fixé avant le held-out et avec le traitement prévu des comparaisons multiples ; taille d’effet et utilité distinguées ; censure et dépendances ne renversant pas la conclusion |
| **Déclarer une amélioration économique** | Gain net documenté avec plans ex ante et contraintes communes ; incertitude statistique et hypothèses d’exécution compatibles avec la conclusion |
| **Autoriser des alertes d’achat V2** | Décision distincte après validation technique et économique, lecture réelle du compte démontrée, plans/contraintes vérifiés et disponibilité mesurée ; les variantes support/reprise ont leurs propres preuves, sans promotion par héritage |
| **Autoriser les alertes de gestion de positions** | Validation du monitoring, compte/plans fiables, tests de panne et de livraison, fonctionnement réel en lecture seule ; cela ne dépend pas de la rentabilité démontrée de V2 |

Un meilleur rappel ne sera pas présenté comme une meilleure rentabilité. Une moyenne positive sur quelques trades ne suffira pas à autoriser les achats.

Les probabilités +10/+20/+30/+40 % restent indisponibles. Une éventuelle calibration devra disposer de ses propres données hors développement et de contrôles de fiabilité.

### P3.8 — Mise en œuvre et acceptation du protocole

**Fichiers proposés.** Nouveau `research/comparison.py`, tables versionnées dans l’index reconstructible, nouveau `tests/test_comparison.py`, spécification dans `docs/EVALUATION.md`.

**Tests.**

- Rejouer deux politiques identiques : différence exactement nulle.
- Dupliquer tous les scans : ne pas doubler artificiellement les épisodes ou la confiance.
- Décaler `policy_ready_at` : aucun remplissage avant disponibilité.
- Ajouter des résultats manquants : censure accrue, sans fabrication de FP/TN.
- Masquer les labels futurs : décisions strictement inchangées.
- Réordonner l’ingestion : résultats identiques.
- Rejouer erreurs de politique, ambiguïtés de remplissage et coûts.
- Même décision et données, seule `data_policy` différente : attribution et états restent explicitement séparés.
- Une politique native plus lente perd le délai utile concerné sans retarder artificiellement sa concurrente.
- Un défaut de collecte avec label positif observable compte dans le bilan end-to-end et dans sa composante sans données exploitables, une seule fois.
- Un futur manquant reste censuré dans les deux métriques de FN ; un veto de décision ne modifie pas le masque de données exploitables.
- Une période sans scan ne disparaît pas de la mesure de couverture et de cadence.
- Une sélection correcte perdue à la publication produit un FN end-to-end d’intégration, sans produire un FN décisionnel.

**Acceptation.** Tout chiffre publié doit pouvoir être reconstruit à partir d’un manifeste de données, de politiques et d’évaluation. Les résultats anciens et corrigés restent séparables.

**Rollback.** Désactiver le nouveau rapport comparatif ; conserver les sources et les journaux permettant sa reconstruction.

## P4 — Optimisations opérationnelles

### P4.1 — Trois chemins d’exécution suffisent initialement

| Chemin | Responsabilité | Dépendances autorisées |
|---|---|---|
| **Supervision critique** | Compte, positions, sorties, éventuel achat admissible, état privé | Code validé, données privées fraîches ; manifeste public optionnel pour les achats |
| **Prospection** | Collecte, V4, instantané, diagnostics, décisions shadow, publication du scan | Données publiques et états antérieurs |
| **Évaluation historique** | Reconstruction/indexation, labels matures, comparaisons, rapports | Journaux publiés et politiques identifiées |

Il n’est pas nécessaire de créer immédiatement un service pour chaque module.

Dans la prospection :

- conserver une collecte légère sur l’univers déclaré ;
- renouveler les profils journaliers selon leur propre échéance ;
- borner les enrichissements et rendre les marchés non enrichis visibles ;
- donner aux candidats à revalider une priorité explicite, sans abandonner silencieusement le reste de l’univers ;
- exécuter le replay du scan nécessaire à la validation ;
- publier les sorties V4 valides même si un runner shadow échoue, avec l’échec shadow identifié ;
- déplacer l’évaluation de tout l’historique hors de ce chemin.

Le replay historique exhaustif peut être périodique ; le contrôle requis avant une nouvelle proposition d’achat reste obligatoire.

### P4.2 — Publication et concurrence

**Correction proposée.** Chaque chemin possède sa liste de fichiers de sortie. Le code exécuté reste dans son checkout figé ; seul le checkout de publication peut être rebasé.

Le manifeste publié lie :

- le scan ;
- les empreintes des sorties ;
- les versions de code et de politiques ;
- le résultat du replay ;
- les heures de disponibilité.

Le monitoring ne doit pas assembler des fichiers « latest » issus de scans différents.

**Fichiers.** `scripts/publish_data.py`, `.github/workflows/update.yml`, nouveaux workflows de monitoring et d’évaluation, tests de publication.

**Acceptation.**

- Conflits sur fichiers distincts : aucune perte.
- Conflits sur le même état : arrêt explicite, jamais écrasement automatique.
- Aucun force-push.
- Aucun achat sur un manifeste incomplet ou périmé.
- Un conflit de publication de prospection ne bloque pas une sortie de position.
- Un échec de persistance après SMTP reste explicitement incertain : pas de fausse garantie de livraison exactement une fois.

**Rollback.** Revenir à la dernière configuration de publication validée, sans changer les journaux ni le code déjà chargé par le monitoring.

### P4.3 — Cadence mesurée sur les décisions effectivement utilisables

L’objectif est une supervision réellement disponible, pas la présence d’un cron de cinq minutes. Le code actuel dépend encore d’un job partagé et la mesure initiale concernait les déclenchements du workflow, pas une preuve de surveillance effective de positions privées.

**Mesures prioritaires.**

- Intervalle entre deux évaluations de positions effectivement réussies, avec p50, p95 et plus longue interruption.
- Âge du compte et du carnet au moment de la décision puis du contrôle final avant notification ; conserver l’horodatage du contenu serveur lorsqu’il est disponible et pertinent, pas seulement l’heure locale de téléchargement.
- Couverture des positions détenues et proportion de cycles dont les données nécessaires sont utilisables.
- Durée des interruptions, échecs et périodes `UNCONFIGURED`. Un heartbeat sans lecture du compte ne prouve pas la supervision des positions.

Décomposer ensuite retard de déclenchement, acquisition, enrichissement, calcul, publication et traitement des positions pour identifier la cause des écarts. Utiliser les durées monotones dans un processus, les horodatages UTC et leur incertitude entre processus.

**Objectif opérationnel conservé comme cible à valider :** sur sept jours, p95 des intervalles de supervision réussie ≤ cinq minutes et aucune interruption > dix minutes. Les limites actuelles de fraîcheur nécessaires aux décisions restent inchangées. Le respect de la cadence ne garantit pas qu’un stop pourra être exécuté sans gap ni retard humain.

La documentation GitHub prévoit des déclenchements retardés et parfois supprimés sous forte charge. Le cron actuel est déjà décalé de la minute zéro ; multiplier les expressions cron ne démontre pas une correction. [Documentation GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

**Décision d’exploitation.** Si les mesures échouent à satisfaire l’exigence, conserver la même logique de monitoring validée et déplacer seulement son déclenchement/exécution vers un hôte durable approprié. L’accès à cet hôte, l’état chiffré courant, la persistance et l’unicité de l’expéditeur sont des dépendances explicites ; aucun hôte disponible n’est présumé.

**Acceptation de la transition.** Aucun double expéditeur, conservation des identifiants de livraison, code validé identifiable, état courant préservé, et cadence mesurée sur des lectures réellement valides. Un changement de scheduler pendant le pilote reste du développement ; ses résultats ne sont pas fusionnés silencieusement avec le held-out figé.

**Rollback.** Revenir au dernier environnement de supervision validé avec l’état courant et rendre l’interruption visible. Ne pas prétendre qu’un ordonnanceur connu comme insuffisant satisfait l’objectif.

### P4.4 — Stockage et coût de calcul

Conserver les journaux compressés comme référence et utiliser un index SQLite incrémental jetable.

L’index enregistrera les identifiants et empreintes des journaux déjà ingérés. Il devra :

- reprendre après interruption ;
- refuser une divergence silencieuse ;
- être entièrement reconstructible ;
- produire les mêmes résultats qu’une reconstruction complète.

**Tests / acceptation.** Ingestion incrémentale, interruption/reprise et reconstruction complète donnent les mêmes données et métriques. La corruption du cache d’index ne modifie aucun journal.

La migration vers un autre stockage n’est pas justifiée dans ce premier lot. Les mesures de durée et de croissance permettront de décider si elle devient nécessaire.

**Fichiers.** `research/history.py`, runner d’évaluation, workflow dédié, tests d’ingestion et de reprise.

**Rollback.** Supprimer uniquement l’index dérivé et reconstruire depuis les journaux originaux.

## Plan final d’implémentation séquentiel de phase 3

Ce plan décrit les travaux futurs. Le présent arbitrage n’en exécute aucun. Chaque lot doit franchir ses tests et préserver les invariants avant de poursuivre. Les critères détaillés et rollbacks des sections P0–P4 s’appliquent à la séquence ci-dessous.

1. **Fixer les références, invariants et frontières des politiques.** Partir d’une révision identifiée après vérification du diff au début de l’implémentation ; conserver les empreintes V4/V1 et les journaux historiques. Définir les identités `data_policy`, `decision_policy`, `execution_policy`, `evaluation_policy`, les deux comparaisons et les deux dénominateurs de FN. Prévoir le dimensionnement après le pilote, sans figer maintenant 5 % / 80 % / cinq points. Acceptation : toute modification future a une attribution et un périmètre explicites.

2. **Fermer et assainir l’ancien exécuteur — A1/A2.** Liste blanche publique, journal privé et garde centrale contre toutes les mutations. Tester aussi les annulations secondaires, configurations manquantes et états invalides. Vérifier séparément le processus déployé. Acceptation : zéro champ privé publié et zéro mutation sortante. Le registre complet d’exposition est différé ; il ne conditionne pas l’étape suivante. Rollback : publication coupée et exécution fermée.

3. **Isoler le monitoring critique — A5.** Workflow et suite propres, SHA/dépendances validés, code exécuté distinct du checkout de publication, état privé courant et expéditeur unique. Examiner d’abord les alertes de gestion justifiées ; imports et données d’achat optionnels ensuite. Commencer la mesure de cadence ici. Acceptation : matrice de panne shadow/prospection/publication sans suppression d’une alerte de sortie justifiée dans le transport simulé. Rollback : dernier code de monitoring validé, état de livraison courant.

4. **Livrer le noyau temporel minimal — P1.1a.** Contenu et métadonnées liés, identité des réponses consommées, cutoff de disponibilité, horloges par profil, manifestes de versions et lecteurs historiques. Acceptation : deux réponses d’une même URL rejouent les deux consommations correctes ; aucune donnée tardive n’entre dans la décision antérieure. Ne pas développer une infrastructure générale de traçabilité.

5. **Corriger les caches — A3/A4.** Profils journaliers autonomes, fraîcheur des dépendances et sélection de bougies closes selon la réponse source ; renouvellement ou indisponibilité explicite. Conserver les valeurs de TTL et de fraîcheur ainsi que les formules V4. Acceptation : AAA + nouveau marché, frontière de clôture, requête traversante et replay multi-réponses ; mêmes bougies et état donnent les mêmes scores. Rollback : refuser les données ambiguës, conserver les modes identifiés.

6. **Corriger la mesure historique et les artefacts — A9/A10.** Continuité jusqu’au franchissement, fenêtres insuffisantes explicites, contrôles courant/historique séparés et alias documentés. Acceptation : aucun événement court confirmé à travers le trou de 3 h 50 ; une ancienne détection ne disparaît pas parce que le marché sort du top courant. Versionner l’évaluation et conserver les anciens rapports.

7. **Introduire les capacités de données et corriger les contrats — A6/A7.** Séparer structure, entrée, exécution et observabilité des résultats ; inconnus explicites ; spread de sévérité monotone ; vrais statuts et raisons de mèches. Conserver les payloads V1. Acceptation : IOST réel distinct du cas synthétique, entrée par défaut jamais utilisée comme mesure, aggravation du spread ne facilitant pas un achat, absence secondaire ne devenant pas un danger inventé.

8. **Corriger le fallback d’achat — A8.** Liste complète ordonnée, contrôles globaux puis individuels, premier candidat admissible, recontrôle final de fraîcheur, marquage après succès SMTP. Acceptation : AA refusé localement → BB seul ; défaut global → aucun achat ; vente prioritaire → aucun achat ; toujours au plus une nouvelle proposition. Rollback : achats désactivés, suivi des positions préservé.

9. **Introduire DL‑V2 Opportunity en shadow.** Baseline expérimentale, catégories cohérentes, seuils conservés, états inconnus et chronologie explicites ; journaux séparés et `scan_id` transmis au runner. Acceptation technique : replay déterministe, tests de frontières, de répétition et d’absence de route active. Les hypothèses support/reprise sont optionnelles, isolées et sans activation ; elles ne bloquent pas la baseline.

10. **Livrer le comparateur et sa traçabilité utile — P1.1b/P3.** Comparaison à cutoff commun, comparaison native complète, contrastes de `data_policy`, épisodes, censure, FN end-to-end et conditionnels, budgets et portefeuilles théoriques séparés. Acceptation par cas synthétiques avant lecture de performance : politiques identiques, doublons, retards, échecs, données futures masquées, périodes manquées et scénarios d’exécution ambigus.

11. **Alléger les chemins et vérifier l’exploitation — P4.** Sortir l’évaluation exhaustive du cycle de prospection, attribuer les sorties à leurs producteurs et ajouter l’index incrémental reconstructible. Vérifier les publications concurrentes sans force-push ni mélange de scans. Mesurer le monitoring réel ; si nécessaire, préparer son seul changement d’hébergement/scheduler. Acceptation : résultats incrémentaux égaux à la reconstruction complète, code chargé immuable, états préservés et limites de cadence explicitement mesurées. Rollback : index dérivé reconstructible et dernier environnement validé.

12. **Pilote technique, dimensionnement, gel, held-out et décision de promotion séparée.** Estimer les paramètres de disponibilité et de dépendance sur le pilote, justifier le protocole et sa durée, geler toutes les versions, puis collecter le held-out neuf d’au moins trente jours et suffisamment informatif selon le protocole. Valider séparément la lecture réelle du compte et les alertes de gestion. Les achats V2 et les heuristiques nouvelles restent désactivés tant que leurs propres critères ne sont pas satisfaits. Une conclusion indéterminée maintient le shadow ; aucun ordre automatique n’est ajouté.
