import * as _ from 'lodash';
import moment from 'moment';

// Serialize a client for response
export function serialize(client) {
    const attributes = _.chain(client)
        .omit('id')
        .assign({
            created_at: moment(client.created_at).utc().format('YYYY-MM-DDTHH:mm:ss[Z]'),
            updated_at: moment(client.updated_at).utc().format('YYYY-MM-DDTHH:mm:ss[Z]')
        })
        .value();

    return {
        type: 'clients',
        id: client.id.toString(),
        attributes: attributes
    };
}

// deserialize a client from json-api
export function deserialize(client) {
    return _.assign(client, {
        created_at: new Date(client.created_at),
        updated_at: new Date(client.updated_at)
    });
}
