# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T18:20:29.495454+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ICNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.462 | entrée 6.250 | trend 8.750 | rang 7.393
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : CTR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.852 | entrée 5.400 | trend 8.500 | rang 7.281
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICNT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.393
2. STX-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.287
3. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.281

## Accélération indépendante

- MEGA-EUR — CONFIRMED_ACCELERATION — score 9.593/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — CONFIRMED_ACCELERATION — score 7.813/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.604/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MEGA-EUR — ACTIVE_NOW — score mémoire 9.593/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- NES-EUR — MEMORY_24H — score mémoire 9.532/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.495/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.033/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — ACTIVE_NOW — score mémoire 7.813/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ZRC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.708/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 7.680/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 7.564/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.473/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICNT-EUR — ACTIVE_NOW — score mémoire 7.393/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- WAL-EUR +58.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +27.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DEEP-EUR +17.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +13.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +13.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXL-EUR +12.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +8.80% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +7.49% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZEUS-EUR +6.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CT-EUR +6.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
