# Export public du pack d’audit Solaire #89

Cet export reprend les fichiers du ZIP final, sans relancer l’audit, modifier ses résultats ou déployer un correctif. Lire d’abord [le rapport final](audit-output/Audit_Solaire_2026-09-27_FINAL.md), [le tableau des 10 actifs](audit-output/Tableau_10_actifs_FINAL.csv) et [le MANIFEST](MANIFEST.md).

Les fichiers `final_*`, `trades_F_*` et `dispositions_F_*` portent les résultats finaux baseline/C1/C2/C3, leurs contrôles négatifs et leurs fenêtres respectives. Les fichiers antérieurs sont conservés pour traçabilité ; leurs métriques ne remplacent pas les résultats finaux. Les configurations et hypothèses de calcul sont dans les scripts figés, notamment `audit-output/replay.py` et `audit-output/finish_audit.py`.

## Intégrité et confidentialité

- `ORIGINAL_ZIP.sha256` : SHA256 du ZIP original de 307 085 231 octets, non committé.
- `ZIP_CONTENTS.csv` : les 734 membres du ZIP, taille, CRC32, SHA256 et statut d’export, y compris tous les membres omis.
- `OMISSIONS.csv` : liste exhaustive, nominative, des 558 omissions avec motif et remplacement/source.
- `SOURCE_ARCHIVES.json` : 547 archives publiques omises, chemins et Git blobs immuables, SHA256 des octets compressés, URL de restauration.
- `CHECKSUMS.sha256` : empreinte de chaque fichier exporté, y compris le MANIFEST, sauf cet index lui-même dont l’intégrité est portée par le commit Git.

Les emails bruts et le contexte de conversation ne sont pas publics. `audit-input/mail_availability.json` conserve les 125 jointures utiles au calcul (timestamp, prix, ID de replay, décalage) mais retire les identifiants Gmail. Ces données permettent de répéter le calcul à partir des timestamps retenus ; elles ne permettent pas de réauthentifier les emails privés. La copie figée `audit-input/scripts/send_production_buy_alert.py` masque une adresse personnelle ; elle sert uniquement à l’inspection, pas à l’exécution. Aucune valeur de credential n’est exportée. Le README original du ZIP est conservé pour traçabilité : ses mentions de preuves privées incluses ne s’appliquent pas à cet export.

Vérification locale sans calcul ni réseau, depuis ce répertoire :

```sh
python3 verify_export.py
```

Le journal V3 est fourni sous `audit-input/solaire_v3_journal.parts/` en 9 fichiers JSONL ordonnés et un fichier de métadonnées, pour respecter la limite de transfert du connecteur. `PARTITIONS.json` documente ce découpage ; `restore_partitions.py` reconstitue exactement les octets originaux et vérifie leur SHA256. Les 4 702 événements sont tous conservés.

## Reproduction facultative dans une copie jetable hors production

Cette procédure est fournie pour la revue externe ; elle n’a pas été exécutée pendant l’export. Python 3 standard et accès réseau public à GitHub sont nécessaires. Prévoir de l’espace pour les archives restaurées et la base dérivée. Ne pas exécuter les copies du scanner ou du sender.

1. Copier ce répertoire dans un répertoire de travail distinct et vérifier les empreintes.
2. Restaurer les 544 archives de marché publiques depuis le ref `0fbc84babfe8567d40979e2a3f695ca57c001182` ; chaque téléchargement est validé par Git SHA1 et SHA256. Les trois échantillons `decision_history` peuvent être restaurés avec `--include-decision-samples`.
3. Reconstruire la base de bougies absente : le script d’origine utilise `archive_summary.json` comme indicateur de cache. Le retirer dans la copie de travail seulement avant de lancer le replay.

```sh
python3 restore_partitions.py
python3 restore_sources.py
python3 -c "from pathlib import Path; Path('audit-output/archive_summary.json').unlink(missing_ok=True)"
python3 audit-output/replay.py
python3 audit-output/evidence.py
python3 audit-output/finish_audit.py
python3 audit-output/gate_details.py
python3 audit-output/priority_replay.py
python3 audit-output/small_size_shadow.py
```

Pour régénérer les textes dans cette copie : `python3 audit-output/make_report.py` puis `python3 audit-output/finalize_report.py`. Certaines sensibilités ont été calculées par appels directs à `replay.simulate(require_trade_bar=True)` ; leurs sorties figées sont incluses. Leur commande exacte d’origine n’est pas consignée dans le pack, et cet export ne prétend pas la reconstituer.

Les résultats sont ceux d’un modèle de fill, pas de transactions réelles. Les limites de données et de causalité restent celles du rapport final. La disponibilité future des sources GitHub n’est pas garantie ; les références immuables et empreintes permettent d’en vérifier les octets tant qu’elles restent accessibles.
