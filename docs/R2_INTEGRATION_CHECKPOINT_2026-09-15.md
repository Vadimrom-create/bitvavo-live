# R2 — intégration contrôlée, avant validation globale R3

## Parents et stratégie

- Main retenu : `c6d891163d82af993635bf38a755fe02ef64aeb7`.
- Main analysé en R1 : `b1b52884417184bc9e248751173e0c4032c7b5ad`.
- Entre ces deux points : uniquement données, états et nouvelles archives ; aucun changement fonctionnel.
- Phase 3 : `2de92fc033c2fff4cbc7dc1f620645a34e65e5aa`.
- Merge-base : `6312a153e80e0e4c9b06c5e6672c541149caefbf`.
- Branche : `codex/astra-phase3-integration-20260915`.
- Fusion sans rebase, conservant exactement les commits Phase 3. Aucun merge vers main.

## Résolutions

La fusion réelle a confirmé six conflits : `pipeline.py`, `research/evaluation.py`,
`scripts/publish_data.py`, `scripts/send_useful_alert.py`, `email_alert_v4.py`,
`.github/workflows/update.yml`.

- Pipeline : version Phase 3 conservée octet pour octet. Acquisition corrigée,
  pointeur explicite du scan, journaux par politique, évaluation exhaustive séparée.
- Évaluation : version Phase 3 conservée octet pour octet, notamment
  `HISTORY_CONTINUITY_V2`. Aucun événement 15 min de main introduit dans les références.
- Alertes et sélecteur : versions Phase 3 conservées octet pour octet. Compte
  inconnu bloque les achats ; sorties prioritaires ; fallback local AA vers BB ;
  une proposition maximum ; marqueurs de livraison après succès SMTP.
- Publication : propriétaires, manifestes, immutabilité, reçus du scan et checkout
  isolé Phase 3 conservés. Ajout des propriétaires `quotes` et `feedback`.
- Workflow : base Phase 3, deux productions facultatives bornées et
  `continue-on-error`. Cotations publiées avant la collecte ; feedback après la
  publication du scan. Aucun commit dans le checkout du code exécuté.

## Dépendances directement adaptées

- `research/feedback_loop.py` de main conservé sans retoucher ses paramètres.
- `research/feedback_diagnostics.py` : enveloppe `FEEDBACK_CAUSAL_V1_SHADOW`,
  contrôle des sources 5m/15m, fraîcheur et clôture ; pas de veto lié au carnet
  ou à l'absence de profil V4 sur ce diagnostic. Attribution descriptive,
  jamais une preuve causale ni une nouvelle métrique de faux négatifs.
- `scripts/run_feedback.py` : scan explicite, copie des observations sans mutation,
  consommation de DL1 seulement si journal et source correspondent ; sinon UNKNOWN,
  sans reconstruction présentée comme historiquement disponible. Date du feedback
  à sa production, distincte de celle du scan. Mémoire par version et data_policy,
  archives immuables, refus des scans antérieurs. Aucun import de la mémoire legacy
  `candidate_memory.json`, qui reste intacte. Aucun routage actif.
- `research/optional_publication.py` : pointeur de succès invalidé avant production,
  manifeste archivé, empreintes des sources/sorties, contrôle du scan courant.
  Échec de production = aucune autorisation de republier les anciens fichiers.
- `scripts/live_quotes.py` : valeurs finies et carnet ordonné ; validité globale
  exigeant au moins un marché valide ; âge calculé sur la source la plus ancienne.
  Limites temporelles de main conservées ; schéma `bitvavo_live_quotes_v2`.
  Nouveau contrôle de fraîcheur avant publication. Aucun seuil V4 modifié.
- `scripts/load_public_state.py` : propriétaire feedback distinct, chargement de
  sa mémoire et de ses archives sans remplacement du code.
- `scripts/prepare_site.py` : sorties optionnelles liées à leur propre manifeste,
  seulement après succès du producteur ; anciennes copies retirées en cas d'échec.
  Une cotation expirée peut donc être absente du site après un scan long, tout en
  ayant été publiée rapidement dans Git ; aucune fraîcheur durable n'est promise.
- `scripts/run_decision_layer.py` : entrée de compatibilité déléguant à run_shadow
  sur runtime/current_scan.json ; suppression de l'inférence du dernier ancien
  journal et du chemin d'écriture dans decision_history.
- README automatiquement fusionné corrigé : suppression de l'annonce d'achats
  publics sans compte ; explication des diagnostics séparés.
- tests/test_positions.py automatiquement fusionné ramené au contrat Phase 3 :
  les attentes d'achat sans compte de main étaient incompatibles avec R1.
- Test de top movers de main adapté au diagnostic séparé ; aucune adaptation des
  références 5m pour faire passer un test prévu pour le détecteur 15m.
- Tests des cotations : horloges synthétiques cohérentes avec les dates de sources.

## Validation R2

Commande exécutée :

```bash
PYTHONPATH=.:tests python -m unittest -q \
  test_r2_integration test_feedback_loop test_live_quotes \
  test_evaluation_contract test_buy_fallback test_positions \
  test_monitor_isolation test_publication test_manifest \
  test_evaluation_runner test_phase3_contract test_index test_pipeline_replay
```

**78 tests réussis.** Dont 16 nouveaux tests de jonction dans test_r2_integration.
Couverture : erreurs facultatives, sources/sorties altérées, mémoire séparée,
réexécution idempotente, scans hors ordre, historique intact, données diagnostiques
sans carnet, fraîcheur/clôture, décision reconstruite vs enregistrée, cotations
non finies/inversées/périmées, anciens rapports non republiés, publication dans un
checkout isolé vers un remote temporaire, nettoyage du site, interface DL1.
Les suites existantes couvrent aussi compte absent, fallback, tous refusés,
sortie malgré panne d'enrichissement, SMTP, continuité et censure des événements.

Le test_pipeline_replay exécute deux scénarios synthétiques hors réseau (legacy et
corrigé) et démontre la parité V4 sur ces scénarios. Cela ne remplace pas les replays
historiques globaux R3. Les 328 objets du contrat de référence passent ; aucun
journal history/ ou decision_history/ n'est changé par rapport au parent main.
Code V4, politiques, DL1 et version épinglée du monitoring inchangés depuis Phase 3.

## Reprise R3 — non effectuée dans R2

- Revalider le commit d'intégration et son état propre.
- Validation globale, replays DL-V1 complets (dont les 113 références initiales),
  replays historiques V4, contrôles CI et comportement opérationnel sur le code publié.
- Vérifier les sorties réelles et la cadence ; aucune collecte réelle ni preuve
  de performance n'est affirmée par R2.
- Le monitoring reste épinglé à `e4d2f2c7b5c040ee102da24208f4cd3ed5aa92c9` ; ne pas
  confondre code intégré et code déployé. Configuration privée :
  **PENDING PRIVATE CONFIGURATION**.
- DL-V2 et feedback exclusivement shadow ; aucune validation held-out réalisée.
- Aucun seuil optimisé ni politique active ajoutée. Aucun merge vers main autorisé
  par ce checkpoint. Publication éventuelle uniquement de la branche d'intégration.

Rollback : ne pas déployer la branche avant R3. Si l'intégration est ultérieurement
publiée dans main, un revert explicite du merge devra préserver les journaux et
états accumulés ; pas de reset, de force-push ou de réécriture historique.
