import click


@click.group()
def cli():
    """Command line wrapper over http://memegenerator.net API"""
    pass


@click.command('generators-search')
@click.option('--q', required=True)
@click.option('--page-index')
@click.option('--page-size')
def generators_search(q, page_index, page_size):
    """generators_search docstring"""
    click.echo('running generators_search...')

@click.command('generators-select-by-popular')
@click.option('--page-index')
@click.option('--page-size')
@click.option('--days')
def generators_select_by_popular(page_index, page_size, days):
    """generators_select_by_popular docstring"""
    click.echo('running generators_select_by_popular...')


@click.command('generators-select-by-new')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
def generators_select_by_new(page_index, page_size):
    """generators_select_by_new docstring"""
    click.echo('running generators_select_by_new...')


@click.command('generators-select-by-trending')
def generators_select_by_trending():
    """generators_select_by_trending docstring"""
    click.echo('running generators_select_by_trending...')


@click.command('generators-select-related-by-display-name')
@click.option('--display-name', required=True)
def generators_select_related_by_display_name(display_name):
    """generators_select_related_by_display_name docstring"""
    click.echo('running generators_select_related_by_display_name...')


@click.command('generators-select-by-url-name-or-generator-id')
@click.option('--url-name', required=True)
@click.option('--generator-id', type=int)
def generators_select_by_url_name_or_generator_id(url_name, generator_id):
    """generators_select_by_url_name_or_generator_id docstring"""
    click.echo('running generators_select_by_url_name_or_generator_id...')


@click.command('instances-select-by-popular')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
@click.option('--url-name')
@click.option('--days', type=int)
@click.option('--language-code', default='en')
def instances_select_by_popular(page_index, page_size, url_name, days,
                                language_code):
    """instances_select_by_popular docstring"""
    click.echo('running instances_select_by_popular...')


@click.command('instances-create')
@click.option('--username', required=True)
@click.option('--password', required=True)
@click.option('--generator-id', type=int, required=True)
@click.option('--image-id', type=int, required=True)
@click.option('--text-0', required=True)
@click.option('--text-1', required=True)
@click.option('--language-code', default='en', required=True)
def instances_create(username, password, generator_id, image_id, text_0,
                     text_1, language_code):
    """instances_create docstring"""
    click.echo('running instances_create...')


@click.command('instances-select-by-new')
@click.option('--page-index', type=int)
@click.option('--page-size', type=int)
@click.option('--url-name')
@click.option('--language-code', default='en')
def instances_select_by_new(page_index, page_size, url_name, language_code):
    """instances_select_by_new docstring"""
    click.echo('running instances_select_by_new...')


@click.command('instances-select')
@click.option('--instance-id', type=int, required=True)
def instances_select(instance_id):
    """instances_select docstring"""
    click.echo('running instances_select...')


@click.command('content-flag-create')
@click.option('--content-url', required=True)
@click.option('--reason', required=True)
@click.option('--email', required=True)
def content_flag_create(content_url, reason, email):
    """content_flag_create docstring"""
    click.echo('running content_flag_create...')


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
