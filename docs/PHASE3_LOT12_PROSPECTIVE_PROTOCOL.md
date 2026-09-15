# Étape 12 — pilote technique et préparation de la validation future

Référence : `ASTRA_PHASE3_RECONCILED_PLAN_2026-09-11.md`, P3.6–P3.8 et étape 12. Cette livraison réalise la partie technique autorisée : inscription prospective, instrumentation descriptive, préparation du protocole et mécanisme de gel. Elle ne réalise ni un held-out, ni une validation de supériorité, ni une promotion. Le plan ne comporte pas d'étape 13.

## Inscription et conservation

Le workflow de prospection ouvre la session **avant** l'acquisition, puis inscrit le scan explicite après le passage par les étapes de décision et de publication. Les étapes du pilote sont facultatives, bornées et indépendantes du monitoring critique. Un scan effectivement produit peut être inscrit même si sa publication ou une branche shadow échoue ; le rapport expose alors les sources/comparaisons manquantes et les livraisons inconnues.

La session lie une empreinte des objets Git du code, des configurations, dépendances et workflows, les identités séparées `data_policy`, `decision_policy`, `execution_policy`, `evaluation_policy`, la spécification de comparaison, les hypothèses d'exécution et les octets exacts de l'amorçage public. Aucun état privé de compte n'est exporté. Un code non commité est refusé. Les commits ne changeant que les données ne changent pas cette empreinte ; une modification du code crée une nouvelle cohorte. Un nouvel évaluateur ne réinterprète pas une cohorte d'une autre version.

Seuls des scans `live` / `TECHNICAL_PILOT` acquis après le début de session sont admissibles. Les replays et fixtures restent du développement. L'inscription est immuable et idempotente ; une collision ou une modification de source est refusée. Les journaux sont conservés dans `prospective_sessions/` et `prospective_observations/`. Les états `runtime/` et l'index SQLite sont dérivés et reconstructibles.

## Rapport et protection de publication

L'évaluation exhaustive demeure hors du cycle de prospection. Le rapport prospectif utilise les cohortes inscrites, leurs comparaisons à cutoff commun et natives, les reçus de publication réellement disponibles et les labels observables de l'index. Il conserve les empreintes des sources, inscriptions, reçus et sources de labels. Les archives de rapport sont immuables dans `prospective_reports/` ; `prospective_report.json` expose l'identifiant et l'heure de génération du dernier rapport réussi.

La publication historique `--evaluation` ne possède aucun fichier prospectif. `run_prospective.py report --publish` publie uniquement le rapport retourné avec succès par cette invocation et son archive exacte, après vérification de leur concordance. Un échec ne repousse aucun ancien rapport. L'artefact GitHub prospectif est lui aussi conditionné au succès de cette étape. Un ancien rapport déjà publié peut rester consultable avec son ancien identifiant et sa date ; il n'est pas annoncé comme résultat du nouveau cycle.

## Instrumentation de dimensionnement

- Fréquence calendaire des épisodes et des épisodes positifs, fraction de labels observables et paires discordantes.
- Différences appariées DL-V2–V4 et DL-V2–DL-V1, séparément à cutoff commun et en mode natif ; variance descriptive, paires inconnues et censure explicites.
- Blocs temporels regroupant les marchés, dispersion, corrélations descriptives temporelles et intermarchés lorsque calculables. Les scénarios 4 h, 24 h et 72 h ne constituent pas des longueurs scientifiquement validées ; les marchés et scans ne sont pas déclarés indépendants.
- Intervalles réels entre scans disponibles, âge du dernier scan, couverture des comparaisons, capacités manquantes, délais de disponibilité et de publication par politique. Une période sans scan conserve des résultats inconnus ; aucun événement non observé n'est inventé.

Les résultats restent `TECHNICAL_PILOT_DEVELOPMENT_ONLY`. Aucun effectif recommandé, intervalle de confiance, probabilité calibrée ou déclaration de supériorité n'est produit. Le gain favorable du pilote ne dimensionne pas automatiquement la validation. La cadence du monitoring des positions reste mesurée par son dispositif propre et ne se déduit pas de la cadence des scans.

## Protocole et gel futurs

Après déploiement du code commité, les workflows peuvent accumuler les nouvelles données publiques du pilote. Les commandes locales équivalentes, à exécuter seulement sur une candidate commitée et avec ses données, sont :

```bash
python scripts/run_prospective.py start
# Acquisition réelle et comparaisons du workflow sur le scan explicite.
python scripts/run_prospective.py record
python scripts/run_prospective.py report
```

Le modèle `config/pilot_protocol_template.json` est volontairement incomplet et ne peut pas être gelé. Préparer une copie séparée, par exemple `runtime/validation_protocol.json`, afin de ne pas modifier la candidate en renseignant le protocole. Justifier le contraste principal, le rappel à budget trois, l'effet utile, le risque d'erreur, la précision visée, la multiplicité, l'effectif informatif, les blocs et sensibilités, les coûts/retards et la durée. Les choix 5 %, 80 % ou cinq points ne sont pas imposés. Le contrôle logiciel vérifie les champs et les bornes ; il ne remplace pas une justification statistique contradictoire du dimensionnement.

Le gel exige un rapport prospectif archivé de la même candidate, une variance appariée estimable, des sources inchangées et une liste d'inscriptions encore à jour. Utiliser son archive immuable, et non le fichier latest :

```bash
python scripts/run_prospective.py freeze \
  --protocol runtime/validation_protocol.json \
  --pilot-report prospective_reports/IDENTIFIANT_DU_RAPPORT.json.gz
```

Le manifeste `prospective_freezes/` conserve code, politiques, hypothèses, protocole et amorçage public. La durée planifiée doit couvrir au moins trente jours neufs ; le démarrage est futur, après maturité du dernier cutoff de développement et embargo au moins égal à l'horizon maximal. Le contrôle d'éligibilité refuse un scan sans cohorte gelée explicite, hors fenêtre, d'une autre version ou présentant un chevauchement de labels de développement.

Le manifeste reste `FROZEN_PROTOCOL_NOT_ACTIVATED`. Aucun workflow de cette livraison n'active une collecte held-out ou ne déclare le pilote held-out. L'ouverture future exige une activation distincte, la vérification du protocole et de l'amorçage, puis de nouvelles données. L'analyse attend la date préenregistrée et le seuil d'information. Une information insuffisante donne une conclusion indéterminée, sans prolongation automatique ni arrêt au premier résultat favorable.

## Invariants, limites et rollback

V4 gelée, ses règles, seuils, poids, références et DL-V1 restent inchangés. Aucun journal historique n'est réécrit. Opportunity-only reste une baseline expérimentale exclusivement shadow. Aucun raccordement aux achats, aucune route active support/reprise, aucun ordre Bitvavo et aucune dépendance du monitoring au module prospectif ne sont ajoutés.

Les tests utilisent des fixtures explicitement synthétiques et des dépôts temporaires ; ils prouvent les contrats techniques, pas une collecte prospective déjà exécutée. Cette session ne déploie pas les workflows et ne pousse pas sur GitHub. L'authentification Git locale reste nécessaire pour publier le commit. La lecture réelle du compte, la fraîcheur/couverture des positions, la cadence opérationnelle et la livraison effective des alertes restent **PENDING PRIVATE CONFIGURATION** et requièrent des accès read-only configurés hors dépôt et hors logs.

Rollback : désactiver uniquement les étapes facultatives du pilote et du rapport prospectif ; conserver sessions, inscriptions, archives, reçus et manifestes. Les index dérivés peuvent être reconstruits. Garder le monitoring isolé et le dernier environnement validé. Aucun rollback ne réécrit les données ni ne promeut DL-V2.

La partie technique de l'étape 12 termine les implémentations de cette phase. Le pilote réel, son dimensionnement contradictoire, le gel effectif, le held-out futur et toute décision de promotion demeurent des validations temporelles ultérieures.
