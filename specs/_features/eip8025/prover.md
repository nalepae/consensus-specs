# EIP-8025 -- Honest Prover

*Note*: This document is a work-in-progress for researchers and implementers.

## Table of contents

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
- [Helpers](#helpers)
  - [New `get_execution_proof_signature`](#new-get_execution_proof_signature)
  - [Constructing and broadcasting the `SignedExecutionProof`](#constructing-and-broadcasting-the-signedexecutionproof)

<!-- mdformat-toc end -->

## Introduction

This document represents the prover guide accompanying EIP-8025. Provers are
active validators who voluntarily generate and submit execution proofs without
direct protocol-level compensation. They provide a public good by enabling
stateless validation during the optional proof phase.

*Note*: Provers are a transitional mechanism. In future mandatory proof forks,
builders will be required to produce and gossip execution proofs as part of
their block production duties, and the prover role will be deprecated.

*Note*: This specification is built upon [Fulu](../../fulu/beacon-chain.md) and
imports proof types from [proof-engine.md](./proof-engine.md).

## Helpers

### New `get_execution_proof_signature`

```python
def get_execution_proof_signature(
    state: BeaconState, proof: ExecutionProof, privkey: int
) -> BLSSignature:
    domain = get_domain(state, DOMAIN_EXECUTION_PROOF, compute_epoch_at_slot(state.slot))
    signing_root = compute_signing_root(proof, domain)
    return bls.Sign(privkey, signing_root)
```

### Constructing and broadcasting the `SignedExecutionProof`

An honest prover that wants to generate execution proofs for beacon blocks
coordinates with a beacon node and validator client as follows:

The prover:

1. subscribes to beacon node SSE block events via
   `GET /eth/v1/events?topics=block`.
2. fetches the blinded block via `GET /eth/v1/beacon/blinded_blocks/{slot}`.
3. extracts `NewPayloadRequest` from `BeaconBlock`:
   - `execution_payload = block.body.execution_payload`
   - `versioned_hashes = [kzg_commitment_to_versioned_hash(c) for c in block.body.blob_kzg_commitments]`
   - `parent_beacon_block_root = block.parent_root`
   - `execution_requests = block.body.execution_requests`
4. generates a `ExecutionProof` zkVM proof.
5. requests a `SignedExecutionProof` to the validator client via
   `POST /eth/v1/validator/execution_proofs`.

Upon receiving each `ExecutionProof`, the validator client:

1. sets message to the `ExecutionProof` and `validator_index` to the prover's
   validator index.
2. signs the proof using
   `get_execution_proof_signature(state, proof, prover_privkey)`.
3. returns the signed proof to the beacon node.

Upon received each `SignedExecutionProof`, the beacon node

1. checks the proof is not a duplicate (same `new_payload_request_root`,
   `proof_type`).
2. broadcasts the proof to the P2P network on the `execution_proof` gossip
   topic.
