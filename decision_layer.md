# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-05T22:01:41.630188+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : FET-EUR | action ACHETE_MAINTENANT | opportunité 8.024 | entrée 7.500 | trend 9.200 | rang 8.014
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : C-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.845 | entrée 6.000 | trend 8.950 | rang 7.671
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : API3-EUR | action LATENT_ACCELERATOR | opportunité 8.388 | entrée 5.550 | trend 9.200 | rang 7.792
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : AXS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.330 | entrée 6.750 | trend 8.650 | rang 7.758
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. FET-EUR — ACHETE_MAINTENANT — rank 8.014 — opportunité 8.024 — entrée 7.500 — trend 9.200
2. WLD-EUR — ACHETE_MAINTENANT — rank 7.734 — opportunité 8.222 — entrée 7.400 — trend 8.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.014
2. API3-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.792
3. AXS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.758

## Accélération indépendante

- ORCA-EUR — CONFIRMED_ACCELERATION — score 7.254/10 — DETECTED_BUT_TOO_LATE
- IMX-EUR — BUILDING_ACCELERATION — score 6.184/10 — DETECTED_BUT_TOO_LATE
- RPL-EUR — BUILDING_ACCELERATION — score 5.975/10 — DETECTED_BUT_TOO_LATE
- RLC-EUR — BUILDING_ACCELERATION — score 5.705/10 — DETECTED_BUT_TOO_LATE
- RAD-EUR — BUILDING_ACCELERATION — score 5.351/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- EDU-EUR — MEMORY_24H — score mémoire 9.962/10 — sources ACCELERATION — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 8.838/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- UMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SWELL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZKP-EUR — MEMORY_24H — score mémoire 8.310/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.233/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 8.155/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PORTAL-EUR — MEMORY_DECAY_24_72H — score mémoire 8.080/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.050/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- RLC-EUR +96.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +78.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RAD-EUR +29.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NIL-EUR +28.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +22.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PNT-EUR +22.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVR-EUR +18.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +16.14% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DIA-EUR +14.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ORCA-EUR +14.16% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
