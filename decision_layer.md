# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-08T20:04:20.975468+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : MEGA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.188 | entrée 6.850 | trend 8.200 | rang 7.050
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.050
2. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.417
3. ICNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.144

## Accélération indépendante

- GNS-EUR — CONFIRMED_ACCELERATION — score 6.780/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — BUILDING_ACCELERATION — score 5.266/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ICNT-EUR — BUILDING_ACCELERATION — score 5.257/10 — DETECTED_BUT_TOO_LATE
- GROVE-EUR — BUILDING_ACCELERATION — score 5.224/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RSR-EUR — BUILDING_ACCELERATION — score 4.800/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- DGB-EUR — MEMORY_DECAY_24_72H — score mémoire 9.295/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 8.877/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.694/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.777/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.050/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — MEMORY_24H — score mémoire 7.048/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BLEND-EUR — MEMORY_24H — score mémoire 6.827/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 6.780/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BOB-EUR — MEMORY_DECAY_24_72H — score mémoire 6.493/10 — sources ACCELERATION — MEMORY_ONLY
- ACT-EUR — MEMORY_24H — score mémoire 6.484/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- GNS-EUR +57.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +19.84% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- BLEND-EUR +13.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +12.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +12.31% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- MERL-EUR +8.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +7.19% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +6.99% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TREAD-EUR +6.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DGB-EUR +5.61% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
