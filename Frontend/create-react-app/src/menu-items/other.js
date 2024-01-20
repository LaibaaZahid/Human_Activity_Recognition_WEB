// assets
/*import { IconBrandChrome, IconHelp } from '@tabler/icons';

// constant
const icons = { IconBrandChrome, IconHelp };*/

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const other = {
  id: 'sample-docs-roadmap',
  type: 'group',
  children: [
    {
      id: 'sample-page',
      title: 'Users',
      type: 'item',
      url: '/sample-page',
      /*icon: icons.IconBrandChrome,*/
      breadcrumbs: false
    },

    {
      id:'connection-page',
      title:'Server Connection',
      type:'item',
      url:'/server-connection-page',
      breadcrumbs: false
    }

  ]
};

export default other;
