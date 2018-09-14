#!/usr/bin/env python

import argparse
import blocwatch_v1.blocwatch_client

def main():
    block_id = ('000000000000000000'
                '168f72be73e69f165a4705314d5e1c9614685413449b07')
    
    client = blocwatch_v1.blocwatch_client.BlocWatchClient()
    
    block = client.bitcoin_blocks.get_block(
            block_id, include=['BASIC', 'SUMMARY', 'DETAILS'])
    print(block)

if __name__ == "__main__":
    main()
