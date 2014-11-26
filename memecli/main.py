import click
import memeapi as meme
import pprint
from tabulate import tabulate


def _print_table(headers, data, keys=None):
    output_data = []
    if keys is None:
        keys = headers
    for d in data:
        row = []
        for key in keys:
            row.append(d[key])
        output_data.append(row)
    output_data.insert(0, headers)
    output = tabulate(output_data, headers='firstrow')
    click.echo(output)


@click.group()
def cli():
    """Command line wrapper over http://memegenerator.net API"""
    pass


@click.command('generators-search')
@click.option('--q', required=True, prompt='Q (search term)')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
def generators_search(q, page_index, page_size):
    """Returns a list of search results filtered by search term."""
    response = meme.generators_search(q=q, page_index=page_index,
                                      page_size=page_size)
    if response['success']:
        headers = ['displayName', 'urlName', 'generatorID', 'imageUrl',
                   'instancesCount', 'ranking', 'totalVotesScore']
        _print_table(headers, response['result'])


@click.command('generators-select-by-popular')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
@click.option('--days', type=int)
def generators_select_by_popular(page_index, page_size, days):
    """Returns the most popular generators for the last n days."""
    response = meme.generators_select_by_popular(
        page_index=page_index, page_size=page_size, days=days
    )

    if response['success']:
        headers = ['ranking', 'displayName', 'urlName', 'generatorID',
                   'imageUrl', 'totalVotesScore', 'instancesCount']
        _print_table(headers, response['result'])


@click.command('generators-select-by-new')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
def generators_select_by_new(page_index, page_size):
    """Returns the most recently created generators."""
    response = meme.generators_select_by_new(page_index=page_index,
                                             page_size=page_size)

    if response['success']:
        headers = ['displayName', 'urlName', 'generatorID', 'imageUrl',
                   'ranking', 'instancesCount', 'totalVotesScore']
        _print_table(headers, response['result'])


@click.command('generators-select-by-trending')
def generators_select_by_trending():
    """Returns recently trending generators."""
    response = meme.generators_select_by_trending()
    click.echo(response)


@click.command('generators-select-related-by-display-name')
@click.option('--display-name', required=True, prompt='Display name')
def generators_select_related_by_display_name(display_name):
    """
    Returns generators that are related to a particular generator, a sort of
    'see also' list.
    """
    response = meme.generators_select_related_by_display_name(
        display_name=display_name
    )
    click.echo(response)


@click.command('generators-select-by-url-name-or-generator-id')
@click.option('--url-name', required=True, prompt='URL name')
@click.option('--generator-id', type=int)
def generators_select_by_url_name_or_generator_id(url_name, generator_id):
    """
    Returns information about a specific generator, either by its generator_id
    or by its url_name.
    """
    response = meme.generators_select_by_url_name_or_generator_id(
        url_name=url_name, generator_id=generator_id
    )
    click.echo(response)


@click.command('instances-select-by-popular')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
@click.option('--url-name')
@click.option('--days', type=int)
@click.option('--language-code', default='en')
def instances_select_by_popular(page_index, page_size, url_name, days,
                                language_code):
    """Returns the most popular instances for a particular criteria."""
    response = meme.instances_select_by_popular(
        page_index=page_index, page_size=page_size, url_name=url_name,
        days=days
    )
    click.echo(response)


@click.command('instances-create')
@click.option('--username', required=True, prompt='Username')
@click.option('--password', required=True, prompt='Password')
@click.option('--generator-id', type=int, required=True, prompt='Generator ID')
@click.option('--image-id', type=int, required=True, prompt='Image ID')
@click.option('--top-text', required=True, prompt='Top text')
@click.option('--bottom-text', required=True, prompt='Bottom text')
@click.option('--language-code', default='en')
def instances_create(username, password, generator_id, image_id, top_text,
                     bottom_text, language_code):
    """Creates a captioned image."""
    response = meme.instances_create(
        username=username, password=password, generator_id=generator_id,
        image_id=image_id, text_0=top_text, text_1=bottom_text,
        language_code=language_code
    )
    click.echo(response)


@click.command('instances-select-by-new')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
@click.option('--url-name')
@click.option('--language-code', default='en')
def instances_select_by_new(page_index, page_size, url_name, language_code):
    """Returns recently created instances, for a particular criteria."""
    response = meme.instances_select_by_new(
        page_index=page_index, page_size=page_size, url_name=url_name,
        language_code=language_code
    )
    click.echo(response)


@click.command('instances-select')
@click.option('--instance-id', type=int, required=True, prompt='Instance ID')
def instances_select(instance_id):
    """ Select an instance by its instance id."""
    response = meme.instances_select(instance_id=instance_id)
    click.echo(response)


@click.command('content-flag-create')
@click.option('--content-url', required=True, prompt='Content URL')
@click.option('--reason', required=True, prompt='Reason')
@click.option('--email', required=True, prompt='Email')
def content_flag_create(content_url, reason, email):
    """ Flag content for removal, for cases of harassment etc."""
    response = meme.content_flag_create(content_url=content_url, reason=reason,
                                        email=email)
    click.echo(response)


cli.add_command(generators_search)
cli.add_command(generators_select_by_popular)
cli.add_command(generators_select_by_new)
cli.add_command(generators_select_by_trending)
cli.add_command(generators_select_related_by_display_name)
cli.add_command(generators_select_by_url_name_or_generator_id)
cli.add_command(instances_select_by_popular)
cli.add_command(instances_create)
cli.add_command(instances_select_by_new)
cli.add_command(instances_select)
cli.add_command(content_flag_create)


if __name__ == '__main__':
    cli()
