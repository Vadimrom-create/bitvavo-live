# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-26T11:16:58.315559+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
Aucun candidat ne remplit actuellement un bucket décisionnel.

## Accélération indépendante

- INIT-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- AIXBT-EUR — CONFIRMED_ACCELERATION — score 7.242/10 — DETECTED_BUT_TOO_LATE
- SSV-EUR — CONFIRMED_ACCELERATION — score 6.572/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MOODENG-EUR — BUILDING_ACCELERATION — score 6.235/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 5.706/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- INIT-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- THQ-EUR — MEMORY_24H — score mémoire 9.864/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 9.564/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — MEMORY_24H — score mémoire 8.993/10 — sources ACCELERATION — MEMORY_ONLY
- AIXBT-EUR — ACTIVE_NOW — score mémoire 7.242/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- O-EUR — ACTIVE_NOW — score mémoire 6.849/10 — sources V4 — DETECTED_BUT_TOO_LATE
- KITE-EUR — MEMORY_24H — score mémoire 6.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 6.643/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 6.572/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 6.500/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- SSV-EUR +42.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ELSA-EUR +37.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVE-EUR +35.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +26.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ME-EUR +25.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +23.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MANTRA-EUR +20.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTC-EUR +15.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SEI-EUR +12.83% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NPC-EUR +12.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
