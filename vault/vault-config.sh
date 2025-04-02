#!/bin/bash
vault server -dev &
sleep 5
vault kv put secret/model-service/api-key value=supersecretkey
